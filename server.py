# Import necessary modules from Flask and paho-mqtt
from flask import Flask, render_template, redirect, url_for
import paho.mqtt.publish as publish
import ssl

# Initialize the Flask web application
app = Flask(__name__)

# MQTT Broker configuration (update values with secure credentials you can move senstive details to .env file for better security)
MQTT_HOST = "95bd7f2a55ad4dd799618axxxxxxxx.s1.eu.hivemq.cloud"  # HiveMQ Cloud broker
MQTT_PORT = 8883  # Standard port for MQTT over SSL/TLS
MQTT_USERNAME = "lovxxxx"  # Your MQTT username
MQTT_PASSWORD = "Secxxxx"  # Your MQTT password
MQTT_TOPIC = "presentation/controlsystem"  # MQTT topic to publish slide control commands

# Function to send MQTT command to the broker securely
def send_mqtt_command(command):
    """
    Publishes a single MQTT message to the specified topic using TLS encryption.
    
    Args:
        command (str): The command to send, e.g., 'next', 'prev', 'start', etc.
    """
    publish.single(
        MQTT_TOPIC,
        payload=command,
        hostname=MQTT_HOST,
        port=MQTT_PORT,
        auth={'username': MQTT_USERNAME, 'password': MQTT_PASSWORD},
        tls=ssl.create_default_context()  # Enables SSL/TLS encryption
    )

# Route for the home page which displays control buttons
@app.route("/")
def index():
    """
    Renders the main presentation control page.
    """
    return render_template("index.html")

# Route to go to the next slide
@app.route("/next")
def next_slide():
    """
    Sends the 'next' command to move to the next slide.
    """
    send_mqtt_command("next")
    return redirect(url_for("index"))

# Route to go to the previous slide
@app.route("/prev")
def prev_slide():
    """
    Sends the 'prev' command to go back to the previous slide.
    """
    send_mqtt_command("prev")
    return redirect(url_for("index"))

# Route to start the presentation
@app.route("/start")
def start_presentation():
    """
    Sends the 'start' command to begin the presentation.
    """
    send_mqtt_command("start")
    return redirect(url_for("index"))

# Route to exit/stop the presentation
@app.route("/exit")
def exit_presentation():
    """
    Sends the 'exit' command to end the presentation.
    """
    send_mqtt_command("exit")
    return redirect(url_for("index"))

# Route to go to the current slide
@app.route("/current")
def current_presentation():
    """
    Sends the 'current' command to go to the current slide.
    """
    send_mqtt_command("current")
    return redirect(url_for("index"))

# Run the Flask app
if __name__ == "__main__":
    # Use app.run(debug=True) for debugging during development
    app.run()
