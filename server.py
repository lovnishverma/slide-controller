import os
from flask import Flask, render_template, redirect, url_for
from dotenv import load_dotenv
import paho.mqtt.publish as publish
import ssl

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load MQTT config from environment variables
MQTT_HOST = os.getenv("MQTT_HOST")
MQTT_PORT = int(os.getenv("MQTT_PORT", 8883))  # Default to 8883 if not set
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
MQTT_TOPIC = os.getenv("MQTT_TOPIC")

# Function to send MQTT command securely
def send_mqtt_command(command):
    publish.single(
        MQTT_TOPIC,
        payload=command,
        hostname=MQTT_HOST,
        port=MQTT_PORT,
        auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD},
        tls=ssl.create_default_context()
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/next")
def next_slide():
    send_mqtt_command("next")
    return redirect(url_for("index"))

@app.route("/prev")
def prev_slide():
    send_mqtt_command("prev")
    return redirect(url_for("index"))

@app.route("/start")
def start_presentation():
    send_mqtt_command("start")
    return redirect(url_for("index"))

@app.route("/exit")
def exit_presentation():
    send_mqtt_command("exit")
    return redirect(url_for("index"))

@app.route("/current")
def current_presentation():
    send_mqtt_command("current")
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
