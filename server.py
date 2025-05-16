import os
from flask import Flask, render_template, redirect, url_for, flash, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
import paho.mqtt.publish as publish
import ssl
from random import choice
import string
from dotenv import load_dotenv
import time
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
import threading
import logging

# Load environment variables from .env file
load_dotenv()

# Track the last command time to prevent multiple rapid commands
last_command_time = {}
COMMAND_COOLDOWN = 1.5  # 0.5 second cooldown between commands
command_lock = threading.Lock()

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "default_secret_key")
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

# Initialize extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    mqtt_username = db.Column(db.String(20), unique=True, nullable=False)
    mqtt_password = db.Column(db.String(20), nullable=False)
    mqtt_host = db.Column(db.String(100), nullable=False)
    mqtt_port = db.Column(db.Integer, nullable=False)
    mqtt_topic = db.Column(db.String(100), unique=True, nullable=False)

# Registration form
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    mqtt_host = StringField('MQTT Host', validators=[DataRequired(), Length(max=100)])
    mqtt_port = IntegerField('MQTT Port', validators=[DataRequired(), NumberRange(min=1, max=65535)])
    mqtt_username = StringField('MQTT Username', validators=[DataRequired(), Length(min=2, max=20)])
    mqtt_password = PasswordField('MQTT Password', validators=[DataRequired()])
    mqtt_topic = StringField('MQTT Topic', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

    def validate_mqtt_username(self, mqtt_username):
        user = User.query.filter_by(mqtt_username=mqtt_username.data).first()
        if user:
            raise ValidationError('That MQTT username is taken. Please choose a different one.')

    def validate_mqtt_topic(self, mqtt_topic):
        user = User.query.filter_by(mqtt_topic=mqtt_topic.data).first()
        if user:
            raise ValidationError('That MQTT topic is taken. Please choose a different one.')

# Login form
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

# # Generate random credentials
# def generate_credentials(length=10):
#     characters = string.ascii_letters + string.digits
#     return ''.join(choice(characters) for _ in range(length))

# User loader callback
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Function to send MQTT command securely with debouncing
def send_mqtt_command(command):
    global last_command_time
    
    # Check if this user has sent a command recently
    user_id = current_user.id
    current_time = time.time()
    
    with command_lock:
        if user_id in last_command_time and (current_time - last_command_time[user_id]) < COMMAND_COOLDOWN:
            logger.info(f"Command ignored (too soon): {command} for user {user_id}")
            return False, "Please wait before sending another command"
        
        # Update the last command time for this user
        last_command_time[user_id] = current_time
    
    try:
        publish.single(
            current_user.mqtt_topic,
            payload=command,
            hostname=current_user.mqtt_host,
            port=current_user.mqtt_port,
            auth={'username': current_user.mqtt_username, 'password': current_user.mqtt_password},
            tls=ssl.create_default_context()
        )
        logger.info(f"Sent MQTT command: {command} for user {user_id}")
        return True, f"Command {command} sent successfully"
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Error sending MQTT command: {error_msg} for user {user_id}")
        return False, f"Error sending command: {error_msg}"

@app.route("/")
@login_required
def index():
    return render_template("index.html", username=current_user.username)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
            mqtt_username=form.mqtt_username.data,
            mqtt_password=form.mqtt_password.data,
            mqtt_host=form.mqtt_host.data,
            mqtt_port=form.mqtt_port.data,
            mqtt_topic=form.mqtt_topic.data
        )
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# AJAX endpoint for sending commands
@app.route("/api/command/<cmd>", methods=['POST'])
@login_required
def send_command(cmd):
    valid_commands = ["next", "prev", "start", "exit", "current"]
    if cmd not in valid_commands:
        logger.warning(f"Invalid command received: {cmd} from user {current_user.id}")
        return jsonify({"success": False, "message": "Invalid command"}), 400
    
    try:
        success, message = send_mqtt_command(cmd)
        return jsonify({"success": success, "message": message})
    except Exception as e:
        error_msg = str(e)
        logger.error(f"Unexpected error: {error_msg} for user {current_user.id}")
        return jsonify({"success": False, "message": "An unexpected error occurred"}), 500

# Keep the original routes for backward compatibility
@app.route("/next")
@login_required
def next_slide():
    logger.info(f"User {current_user.id} requested /next")
    success, message = send_mqtt_command("next")
    if success:
        logger.info(f"Command 'next' sent successfully for user {current_user.id}")
    else:
        logger.warning(f"Failed to send command 'next' for user {current_user.id}: {message}")
    return redirect(url_for("index"))

@app.route("/prev")
@login_required
def prev_slide():
    logger.info(f"User {current_user.id} requested /prev")
    success, message = send_mqtt_command("prev")
    if success:
        logger.info(f"Command 'prev' sent successfully for user {current_user.id}")
    else:
        logger.warning(f"Failed to send command 'prev' for user {current_user.id}: {message}")
    return redirect(url_for("index"))

@app.route("/start")
@login_required
def start_presentation():
    logger.info(f"User {current_user.id} requested /start")
    success, message = send_mqtt_command("start")
    if success:
        logger.info(f"Command 'start' sent successfully for user {current_user.id}")
    else:
        logger.warning(f"Failed to send command 'start' for user {current_user.id}: {message}")
    return redirect(url_for("index"))

@app.route("/exit")
@login_required
def exit_presentation():
    logger.info(f"User {current_user.id} requested /exit")
    success, message = send_mqtt_command("exit")
    if success:
        logger.info(f"Command 'exit' sent successfully for user {current_user.id}")
    else:
        logger.warning(f"Failed to send command 'exit' for user {current_user.id}: {message}")
    return redirect(url_for("index"))

@app.route("/current")
@login_required
def current_presentation():
    logger.info(f"User {current_user.id} requested /current")
    success, message = send_mqtt_command("current")
    if success:
        logger.info(f"Command 'current' sent successfully for user {current_user.id}")
    else:
        logger.warning(f"Failed to send command 'current' for user {current_user.id}: {message}")
    return redirect(url_for("index"))

# Serve the HTML file
@app.route('/static/index.html')
def static_index():
    return render_template('index.html', username=current_user.username)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables within the application context
    app.run(debug=True)  # Use a proper WSGI server in production