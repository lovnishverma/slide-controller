# 📄 Documentation: Slide Controller – Revolutionizing Remote Presentation Control with MQTT

## **Created by Lovnish Verma**

This innovative tool offers a cost-effective and customizable solution for remote presentation control, leveraging MQTT for real-time communication.
![slide-controller](https://github.com/user-attachments/assets/5e1088ee-0f61-4086-9516-6475d13f5f83)

---

## 🌟 Introduction

Tired of relying on expensive proprietary devices like the **Hardware Based Wireless Presenters** to control your slides? Meet **Slide Controller** — a cutting-edge, open-source web application that turns your smartphone, tablet, or laptop into a **fully customizable, feature-rich presentation remote** — all for **FREE**!

---

## ✅ Key Features

* 🎨 **Beautiful Responsive UI**: Modern CSS design with cards, shadows, and clean typography.
* ⏭️ **Next/Previous Buttons**: Navigate presentation slides interactively.
* 🟢 **Live Status Indicator**: Real-time MQTT connection status with color-coded indicators.
* 🎛️ **Device Toggle & Sensitivity Slider**: Optional controls for motion/gesture extensions.
* 🌐 **Cross-Platform Access**: Works on mobile, tablet, and desktop browsers.
* 🔌 **Integration Ready**: Extendable for gesture, voice, or IoT triggers.
* 🖥️ **Tkinter GUI (New in v2.0)**: A modern graphical interface for easy configuration and real-time feedback.
* ⚙️ **MQTT Settings Customization (New in v2.0)**: Edit broker, port, username, password, and topic directly from the app without modifying code.

---

## 💡 Why Slide Controller is Revolutionary?

1⃣ **No Hardware Required**

* Forget physical presenters. Use **any internet-connected device** as your remote control. Works on **mobile, tablet, or desktop browsers**.

2⃣ **MQTT-Powered Connectivity**

* Leverages **MQTT**, the industry-standard IoT protocol, for **real-time, low-latency slide transitions**. Unlike traditional remotes, it’s **extendable** to integrate with IoT devices, voice assistants, or even custom hardware.

3⃣ **Motion & Gesture Control**

* **Shake your device** to skip slides or adjust sensitivity via a built-in slider. No need to press buttons—your movements become commands!

4⃣ **Haptic Feedback**

* Feel vibrations on your device when slides change, ensuring you’re always in sync with your presentation.

5⃣ **Cross-Platform & Open-Source**

* Fully customizable codebase. Tweak UI/UX, add new features (like voice commands or gesture recognition), or integrate it with smart devices—**the possibilities are endless**!

6⃣ **Dark Mode & Responsive Design**

* A sleek, **modern UI** with toggleable dark mode and pixel-perfect responsiveness for **every screen size**.

7⃣ **Tkinter GUI Enhancements (v2.0)**

* Easily configurable MQTT settings
* Visual feedback for connection status
* Support for saving preferences locally using config files
* User-friendly theme switching and window management

---

## 🔧 How It Works

* **Web Interface**: Hosted on platforms like **Glitch**, the frontend provides intuitive controls.
* **MQTT Broker**: Uses **HiveMQ Cloud** or local brokers (like Mosquitto) for reliable communication.
* **Local Automation**: A Python script listens to MQTT messages and uses **`pyautogui`** to simulate keyboard inputs, controlling PowerPoint or any presentation software directly.
* **Subscriber v2.0**: Now comes with a Tkinter GUI to configure:

  * MQTT Broker
  * Port
  * Username
  * Password
  * Topic
  * Themes (Light, Dark, High Contrast)
  * Window always-on-top toggle

---

## 🥺 Features That Set It Apart

| **Unique Features**         | **Traditional Remotes** | **Slide Controller**                 |
| --------------------------- | ----------------------- | ------------------------------------ |
| **Cost**                    | ₹2,500+                 | **FREE** (Open Source)               |
| **Customization**           | Limited buttons         | Add voice/gesture/IoT controls       |
| **Connectivity**            | Wired/Wi-Fi only        | Cross-platform via MQTT              |
| **Feedback**                | None                    | Haptic vibrations + visual cues      |
| **Extensibility**           | Closed ecosystem        | Fully open-source, hackable          |
| **GUI Configuration**       | Not available           | New Tkinter-based GUI for easy setup |
| **Configurable MQTT Setup** | Hardcoded               | Edit credentials live in GUI         |
| **Themes Supported**        | Fixed UI                | Light, Dark, High Contrast           |

---

## 🛠️ Technical Highlights

* **Stack**: HTML/CSS/JS for the frontend, **Python Flask** + **Paho MQTT** for backend, and **PyAutoGUI** for automation.
* **Subscriber v2.0**: Built with **Tkinter**, supports dynamic MQTT configuration and theming.
* **Deployment**: Host the web app on **Glitch** in minutes—no server setup required.
* **Security**: Uses secure MQTT brokers like **HiveMQ Cloud** with TLS encryption.
* **Accessibility**: Works offline (for motion controls) and supports **keyboard shortcuts** for touch-free operation.

---

## 📦 Project Structure (Updated with v2.0) / (Hosted on glitch.com) 

**Source code** in the [GLITCH BRANCH](https://github.com/lovnishverma/slide-controller/tree/glitch)

```
slide-controller/
├── templates/index.html          # Web UI
├── server.py                     # Flask MQTT publisher

```

**Source code** in the [backend-server BRANCH](https://github.com/lovnishverma/slide-controller/tree/backend-server)


```
├── dist/subscriber_version-2.0.exe          # New Tkinter-based MQTT subscriber
└── subscriber_version-2.0.py               # THE EXE file (built from subscriber_version-2.0.py using PyInstaller)
```

---

## 🌐 Set Up MQTT Broker

### ✅ Option 1: HiveMQ Cloud (Recommended)

> HiveMQ Cloud is free, secure, reliable, and requires no local setup.

#### Step-by-Step: Create a HiveMQ Cloud Broker

1. Go to [HiveMQ Cloud Console](https://console.hivemq.cloud/)
2. Sign up or log in
3. Create a new cluster (Free Tier)
4. Note the Broker Hostname and Port (8883 for TLS)
5. Create MQTT Credentials (Username & Password)
6. Enable TLS/SSL

![image](https://github.com/user-attachments/assets/472547c9-3e3b-456b-bea4-a5db7bd801c5)

Example Code:

```python
BROKER = "your-cluster-id.s2.eu.hivemq.cloud"
PORT = 8883
USERNAME = "slideuser"
PASSWORD = "myslidesecret"
TOPIC = "slide/control"

client.tls_set()
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT)
```

### ✅ Option 2: Local Mosquitto Broker (Advanced Users Only)

Install on Linux:

```bash
sudo apt install mosquitto mosquitto-clients
mosquitto
```

Set in scripts:

```python
BROKER = "localhost"
PORT = 1883
```

---

## 🧹 Subscriber v2.0 – Tkinter GUI Details

The new version introduces a **graphical user interface (GUI)** built with **Tkinter**, allowing users to:

### 🔧 MQTT Settings Panel

* Change **Broker Address**
* Modify **Port Number**
* Update **Username** and **Password**
* Set Custom **Topic Name**
* Save settings to a local `.json` file for persistence eg:- mqtt_controller_config.json

### 🎨 Theme Manager

* Switch between:

  * **Light Theme**
  * **Dark Theme**
  * **High Contrast Theme**
* Apply changes instantly without restarting the app

### 📡 Connection Status Indicator

* Visual indicator showing MQTT connection status
* Tooltip shows detailed status messages (e.g., "Connected", "Disconnected", "Auth Failed")

---

## 🚀 Deployment Guide – Slide Controller Web App on Glitch.com (this project is deployed in render.com coz glitch.com is discontinued)

### Step-by-Step Instructions

1. Visit [Glitch.com](https://glitch.com/)
2. Sign up or log in
3. Remix the [Python3 Starter Project](https://glitch.com/~python3flask-python-3)
4. Rename the project (e.g., `slide-controller`)
5. Upload or create:

   * `server.py`
   * `templates/index.html`
   * `requirements.txt`
   * Optional: `.env` for MQTT credentials if you're not using database
6. Start the app and preview

### File Structure Overview

```
/slide-controller (project root)
├── server.py
├── requirements.txt
├── templates/index.html
├── README.md
├── glitch.json
└── .env
```

---

## 🔄 Running the App

### Option 1: Run from Glitch

🚀 Live Demo: [https://slidecontroller.glitch.me](https://slidecontroller.glitch.me)

### Option 2: Run Subscriber Script or Convert to EXE

Install PyInstaller:

```bash
pip install pyinstaller
```

**Note:** To generate icon go to [icoconverter.com](https://www.icoconverter.com/) upload .jpg or .png  and get your icon in .ico format

Convert to executable:

```bash
pyinstaller --onefile --icon=slidecontrol.ico --noconsole subscriber_version-2.0.py
```

Run:

```bash
dist\subscriber_version-2.0.exe
```

---

## 📦 Requirements for Tkinter Version

Install dependencies:

```bash
pip install paho-mqtt pyautogui PyInstaller
```

Or use `requirements.txt`:

```txt
paho-mqtt
pyautogui
PyInstaller
```

---

## 📝 Notes

* The Tkinter GUI saves MQTT settings in a `config.ini` file for persistent configuration.
* Users can now edit MQTT credentials without touching the code.
* Themes are stored in a separate JSON file for easy expansion.
* The GUI supports resizing, minimizing, and staying on top of other windows.
* Ensure the `subscriber.exe` is running with proper screen access and focus on the presentation app (e.g., PowerPoint).

---

## 🧪 Test It Out

1. Open your Flask web app in a browser.
2. Click "Next" or "Previous" buttons.
3. On the presentation computer, ensure `subscriber_version-2.0.exe` is running and PowerPoint is focused.
4. Slide transitions should occur instantly.
5. You can now modify MQTT settings and switch themes on the fly.

---

## 📸 Screenshots

**Slide Controller Flask App using MQTT**
Web UI Running on Android or iOS phone to control host machine:
![image](https://github.com/user-attachments/assets/24111d5c-0497-42dc-aaab-ec9ba812dbf8)

**Subscriber v1.0 GUI Running on Host Machine**
![image](https://github.com/user-attachments/assets/a2d327c5-0461-457e-8442-c6b9d678527c)

**Subscriber v2.0 GUI Running on Host Machine** (Recommended)
![image](https://github.com/user-attachments/assets/9ef79c2f-3eb5-4ab3-a355-b5e379a4e76b)

---

## 📄 Special Note by Author and Maintainer of this project Mr. Lovnish Verma 😉

Do whatever you want, but don't blame us if you break your projector 😉.

---

## 📣 Final Thoughts

> Slide Controller isn't just about replacing a remote—it's about **democratizing control**, enabling anyone with a browser and internet connection to **seamlessly manage presentations**, automate classrooms, and invent new interfaces.

---


### 📚 Resources

🔗 **GitHub Repository**:  
[Slide Controller on GitHub](https://github.com/lovnishverma/slide-controller)  
*Clone or contribute to the open-source project.*

🚀 **Controller Web App (Source Code)**:  
[Remix on Glitch – Slide Controller](https://glitch.com/~slidecontroller)  
> 🔧 **Instructions**:  
- Click **Remix** to create your own copy.  
- Update the credentials in `.env` file with your own.

![image](https://github.com/user-attachments/assets/9b57da93-3d24-447d-8179-6b2dd2f40c8a)


  
- The app will be live at `https://your-project-name.glitch.me`.
- 

Register with your HiveMQ Credentials on this web application: Create Cluster on [HiveMQ](https://www.hivemq.com/)

![image](https://github.com/user-attachments/assets/84547538-007c-40cd-8081-e1f1fece3040)


📥 **Windows Executable (Host Machine)**:  
[Download subscriber2.0.exe](https://www.mediafire.com/file/m5qn77efi33ekcq/subscriber2.0.exe/file)  
> 📝 Default Login (for demo):  
- **Username**: `admin`  
- **Password**: `password`
- Update the HiveMQ credentials from Settings tab

![image](https://github.com/user-attachments/assets/8b04b7ef-ae83-4cf6-9192-6bdedca7da5e)

---
