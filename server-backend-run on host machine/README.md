# Documentation for MQTTSlideControlApp

## Overview

`MQTTSlideControlApp` is a Python Tkinter GUI application that controls a presentation remotely via MQTT messages. It connects securely to an MQTT broker using TLS, subscribes to a specified topic, and listens for commands to simulate keyboard presses using PyAutoGUI for slide navigation.

### Features

* Connect and disconnect from MQTT broker securely (TLS/SSL).
* Send and receive presentation control commands (`start`, `prev`, `next`, `current`, `exit`).
* GUI with three tabs:

  * **Control**: Buttons for manual control of slides.
  * **Settings**: Configure MQTT connection (broker, port, username, password, topic).
  * **Terminal**: View real-time logging output.
* Save and load configuration from JSON file.
* User authentication dialog on startup.
* Robust error handling and status updates.
* Logs displayed live in the GUI terminal.

---

## Installation Requirements

* Python 3.7+
* Required Python packages:

  * `paho-mqtt`
  * `pyautogui`
  * `tkinter` (usually included with Python)
  * `logging` (standard library)
* Optional (for packaging): `pyinstaller`

You can install the required packages via:

```bash
pip install paho-mqtt pyautogui
```

---

## File Structure

* `mqtt_controller_config.json` — Configuration file for MQTT connection (created automatically on first save).
* Your main script, e.g., `subscriber_version-2.0.py` (the provided code).

---

## How It Works

1. **Startup**

   * Application starts with a login dialog for authentication (hardcoded for demo).
   * Loads configuration from `mqtt_controller_config.json` or uses default values.
2. **Connect to MQTT Broker**

   * User clicks "Connect".
   * Application connects using TLS and credentials.
   * Subscribes to the specified MQTT topic.
3. **Control Presentation**

   * Receives MQTT messages with commands like `start`, `prev`, `next`, etc.
   * Simulates keypresses using `pyautogui` to control presentation software.
   * User can also send commands manually via the Control tab buttons.
4. **Settings**

   * User can update connection details and save them.
   * Option to reconnect automatically after saving new settings.
5. **Terminal**

   * Real-time logging output displayed inside the GUI.
6. **Disconnect**

   * User can disconnect from the MQTT broker cleanly.

---

## Important Methods

| Method                  | Description                                                  |
| ----------------------- | ------------------------------------------------------------ |
| `load_config()`         | Loads MQTT config from JSON file or defaults if not found.   |
| `save_config()`         | Saves current MQTT config to JSON file.                      |
| `connect_mqtt()`        | Starts connection to MQTT broker in a background thread.     |
| `disconnect_mqtt()`     | Disconnects from the MQTT broker cleanly.                    |
| `on_connect()`          | MQTT callback when connection is established.                |
| `on_message()`          | MQTT callback when message received; triggers slide actions. |
| `send_command(cmd)`     | Sends a MQTT message with a slide control command.           |
| `create_notebook()`     | Initializes tabbed UI.                                       |
| `create_control_tab()`  | Builds UI for control buttons and connection status.         |
| `create_settings_tab()` | Builds UI for MQTT settings entry and saving.                |
| `create_terminal_tab()` | Builds UI for displaying log output.                         |
| `authenticate_user()`   | Shows login dialog before allowing connection.               |

---

## User Authentication

Currently implemented with a simple dialog:

* Username: `admin`
* Password: `password`

Can be extended for more complex authentication as needed.

---

## Slide Control Commands

| Command   | Action Simulated                      |
| --------- | ------------------------------------- |
| `start`   | Presses F5 to start presentation      |
| `prev`    | Presses Left arrow for previous slide |
| `next`    | Presses Right arrow for next slide    |
| `current` | Presses Shift + F5 for current slide  |
| `exit`    | Presses ESC to exit presentation      |

---

## Usage

1. Run the script:

```bash
python subscriber_version-2.0.py
```

2. Enter login credentials.
3. Go to **Settings** tab and update MQTT broker details if needed.
4. Click **Connect** in the **Control** tab.
5. Use control buttons or listen for incoming MQTT messages to control your presentation.

---

## Troubleshooting

* If the app fails to connect, check network and MQTT broker settings.
* Logs in the **Terminal** tab will show detailed error messages.
* Ensure the MQTT topic matches between publisher and subscriber.
* On Windows, pyautogui requires permissions for simulating keyboard events.

---

# How to Convert This Script to a Windows Executable (.exe)

To convert your Python Tkinter MQTT app into a standalone `.exe`, follow these steps using **PyInstaller**:

---

### Step 1: Install PyInstaller

```bash
pip install pyinstaller
```

---

### Step 2: Prepare Your Script

Make sure your script (e.g., `subscriber_version-2.0.py`) is fully working and all dependencies are installed.

---

### Step 3: Create the Executable

Open a terminal (Command Prompt) in your script directory and run:

```bash
pyinstaller --onefile --icon=slidecontrol.ico --noconsole subscriber_version-2.0.py
```

* `--onefile`: Package everything into a single executable file.
* `--windowed` or `noconsole`: Suppress the console window (good for GUI apps).

---

### Step 4: Locate the Executable

After building, you will find the `.exe` file in the `dist` folder inside your project directory:

```
dist/subscriber_version-2.0.exe
```

---

### Step 5: Test the Executable

Double-click the `.exe` file to run it. The GUI should launch without needing Python installed.

---

### Notes & Tips:

* If you use external files like `mqtt_controller_config.json`, package it alongside or handle config creation on first run.
* For PyAutoGUI to work properly, the executable may need administrator privileges (right-click > Run as Administrator).
* If SSL/TLS certificates cause issues, ensure certificates are accessible in the environment or package them accordingly.
* Use PyInstaller hooks or add data files if you have extra assets or config files.
* For debugging PyInstaller builds, omit `--windowed` to see error messages in console.

---

# Summary

* You now have a fully documented Python MQTT slide controller GUI app.
* Configuration, logging, and user authentication are built in.
* You can package it into a Windows `.exe` with PyInstaller using simple commands.
* The executable is portable and does not require Python on the target machine.

---
