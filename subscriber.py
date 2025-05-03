# mqtt_slide_control.py
import paho.mqtt.client as mqtt
import pyautogui
import ssl

# MQTT Broker Configuration
BROKER = "95bd7f2a55ad4dd799618a9xxxxxxxxx.s1.eu.hivemq.cloud"
PORT = 8883
USERNAME = "lovxxxx"
PASSWORD = "Secxxxx"
TOPIC = "presentation/controlsystem"

# MQTT Callback: On successful connection


def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(TOPIC)

# MQTT Callback: On message received


def on_message(client, userdata, msg):
    command = msg.payload.decode().strip().lower()
    print("Command received:", command)

    if command == "next":
        pyautogui.press("right")
    elif command == "prev":
        pyautogui.press("left")
    elif command == "start":
        pyautogui.press("f5")
    elif command == "exit":
        pyautogui.press("esc")
    elif command == "current":
        pyautogui.hotkey("shift", "f5")
    else:
        print("Unknown command")


# MQTT Client Setup
client = mqtt.Client()
client.username_pw_set(USERNAME, PASSWORD)
client.tls_set(cert_reqs=ssl.CERT_REQUIRED)
client.on_connect = on_connect
client.on_message = on_message

# Connect to MQTT Broker and Start Listening
client.connect(BROKER, PORT)
client.loop_forever()
