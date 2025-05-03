from flask import Flask, render_template, redirect, url_for
import paho.mqtt.publish as publish
import ssl

app = Flask(__name__)

MQTT_HOST = "95bd7f2a55ad4dd799618a95837e4303.s1.eu.hivemq.cloud"
MQTT_PORT = 8883
MQTT_USERNAME = "lovnish"
MQTT_PASSWORD = "Nielit@123"
MQTT_TOPIC = "presentation/control"

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
    app.run()
