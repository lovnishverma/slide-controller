Here’s an enhanced version of your `README.md` file with detailed instructions on setting up an **MQTT Broker**, focusing on **HiveMQ Cloud**, along with complete guidance on creating an account, setting up a broker, and configuring credentials.

---

# 🚀 Slide Controller – Remote Presentation Navigation via MQTT

The **Slide Controller** is a responsive and user-friendly web application that allows seamless **remote navigation of PowerPoint slides over MQTT**. Designed for **presenters, educators, and conference speakers**, the app enables slide control through a web interface that communicates with a local Python MQTT subscriber script which simulates keyboard events to control slide transitions.

---

## ✅ Key Features

* 🎨 **Beautiful Responsive UI**: Modern CSS design with cards, shadows, and clean typography.
* ⏭️ **Next/Previous Buttons**: Navigate presentation slides interactively.
* 🟢 **Live Status Indicator**: Real-time MQTT connection status with color-coded indicators.
* 🎛️ **Device Toggle & Sensitivity Slider**: Optional controls for motion/gesture extensions.
* 🌐 **Cross-Platform Access**: Works on mobile, tablet, and desktop browsers.
* 🔌 **Integration Ready**: Extendable for gesture, voice, or IoT triggers.

---

## 🛠️ How It Works

1. **Frontend (index.html)**: Web UI hosted on **Glitch** acts as the **MQTT publisher**.
2. **Backend (server.py)**: Flask app serves the frontend and publishes MQTT messages.
3. **Local Subscriber (subscriber.py)**: Listens to MQTT messages and uses `pyautogui` to simulate PowerPoint key presses.

---

## 🧰 Tech Stack

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python (Flask), Paho MQTT
* **MQTT Broker**: [HiveMQ Cloud](https://console.hivemq.cloud/), Mosquitto (local), or Adafruit IO
* **Automation**: `pyautogui` for keyboard simulation

---

## 📁 Project Structure

```
slide-controller/
├── index.html          # Web UI
├── server.py           # Flask MQTT publisher
├── subscriber.py       # Python MQTT subscriber
└── slidecontrol.ico    # Optional EXE icon
```

---

## 🔄 Running the App

### 1. 🚀 Start the Flask App

```bash
python server.py
```

Deployed online? Use Glitch or another hosting platform to serve `server.py` and `index.html`.

---

### 2. 💻 Run Subscriber Script

Convert `subscriber.py` to `.exe` using PyInstaller:

```bash
pyinstaller --onefile --icon=slidecontrol.ico subscriber.py
```

Or, if you want to hide the console:

```bash
pyinstaller --onefile --noconsole --icon=slidecontrol.ico subscriber.py
```

Then run:

```bash
dist\subscriber.exe
```

---

## 🌐 Set Up MQTT Broker

### ✅ Option 1: Use HiveMQ Cloud (Recommended)

> HiveMQ Cloud is free, secure, reliable, and requires no local setup.

### 🔐 Step-by-Step: Create a HiveMQ Cloud Broker

1. **Go to HiveMQ Cloud**:
   [https://console.hivemq.cloud/](https://console.hivemq.cloud/)

2. **Sign Up / Log In**:

   * Create a free account or log in.

3. **Create a New Cluster**:

   * Click **"Create New Cluster"**
   * Choose **Free Tier**
   * Name your cluster (e.g., `slide-controller`)
   * Wait 1–2 minutes for provisioning.

4. **View Connection Details**:

   * Once cluster is ready, click **"View Connection Details"**
   * Note the **Broker Hostname** and **Port** (`8883` for TLS)

5. **Create MQTT Credentials**:

   * Go to **Access Management > Credentials**
   * Click **Create New Credential**

     * Choose a **Username** (e.g., `slideuser`)
     * Set a **Password** (e.g., `myslidesecret`)
   * Save these for your `server.py` and `subscriber.py`

6. **Enable TLS/SSL** (Optional but recommended):

   * HiveMQ Cloud requires TLS (port 8883)
   * You must install `paho-mqtt` with TLS support:

     ```bash
     pip install paho-mqtt
     ```

---

### ✅ Example HiveMQ Configuration

In `server.py` and `subscriber.py`, update:

```python
BROKER = "your-cluster-id.s2.eu.hivemq.cloud"
PORT = 8883
USERNAME = "slideuser"
PASSWORD = "myslidesecret"
TOPIC = "slide/control"
```

Also, set up TLS:

```python
client.tls_set()  # Enables TLS
client.username_pw_set(USERNAME, PASSWORD)
client.connect(BROKER, PORT)
```

---

### ⚙️ Option 2: Use Local Mosquitto Broker

#### Install on Windows/Linux:

```bash
sudo apt install mosquitto mosquitto-clients
```

Start broker:

```bash
mosquitto
```

Set `BROKER = "localhost"` and `PORT = 1883` in your scripts.

---

## 🧪 Test It Out

* Open your Flask web app in a browser.
* Click "Next" or "Previous" buttons.
* On the presentation computer, ensure `subscriber.exe` is running and PowerPoint is focused.
* Slide transitions should occur instantly.

---

## 📝 Notes

* You can add gestures, voice, or phone sensors to enhance control.
* Ensure subscriber script runs with proper screen access.
* Web UI can be hosted on any static site host or Glitch.

---

## 📸 Screenshots

![image](https://github.com/user-attachments/assets/24111d5c-0497-42dc-aaab-ec9ba812dbf8)


![image](https://github.com/user-attachments/assets/a2d327c5-0461-457e-8442-c6b9d678527c)

---

**complete Glitch deployment guide** tailored specifically for your **Slide Controller Flask App using MQTT**, perfect for inclusion in your `README.md` or as a separate `glitch-deployment.md`.

---

## 🚀 **Glitch Deployment Guide – Slide Controller Web App**

This guide walks you through **hosting the Flask MQTT Publisher (Web App)** on **Glitch.com**, a free online IDE and hosting platform ideal for quick web app deployment and sharing.

---

### 🔧 **What You’ll Deploy**

You’ll host the `server.py` Flask app (MQTT Publisher) along with its frontend (`index.html`) on Glitch. The app will expose a public URL (e.g., `https://slide-controller.glitch.me`) that can send MQTT messages to your local subscriber script.

---

### ✅ **Step-by-Step Deployment on Glitch**

---

### 1️⃣ **Sign Up or Log In**

* Visit: [https://glitch.com/](https://glitch.com/)
* Click **Sign Up** or **Log In** using GitHub, Google, or email.

---

### 2️⃣ **Create a New Project**

* Click **“New Project” → “Hello-Express”** (Glitch supports Node.js by default).
* Rename the project to something like `slide-controller`.

---

### 3️⃣ **Delete Existing Files**

Delete these default files from Glitch:

* `server.js`
* `package.json`
* `public/`
* `views/`

---

### 4️⃣ **Add Your Flask App Files**

Upload or manually create the following files:

* `server.py` – Your Flask MQTT Publisher code
* `requirements.txt` – Add this content:

  ```txt
  Flask
  paho-mqtt
  ```
* `index.html` – Your frontend controller page
* `start.sh` – A custom shell script to launch your Flask app
* `.glitch-assets` – (optional) For storing any media/assets if needed

#### Example `start.sh` content:

```bash
#!/bin/bash
export FLASK_APP=server.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=3000
pip install -r requirements.txt
flask run
```

Make it executable:

1. Click the **“Tools”** button on the bottom left
2. Open **Terminal**
3. Run:

   ```bash
   chmod +x start.sh
   ```

---

### 5️⃣ **Configure `glitch.json`**

Create a new file called `glitch.json` to tell Glitch how to run your app:

```json
{
  "start": "bash start.sh"
}
```

---

### 6️⃣ **Update `.env` with MQTT Credentials**

In `.env`, add your HiveMQ Cloud credentials or other broker info:

```env
MQTT_BROKER=broker.hivemq.com
MQTT_PORT=1883
MQTT_USERNAME=your-username
MQTT_PASSWORD=your-password
MQTT_TOPIC=slide/control
```

In `server.py`, read them like this:

```python
import os

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
```

---

### 7️⃣ **Start the App**

Once files are ready:

* Click the **“Logs”** button to see output.
* Glitch will auto-run `start.sh`.
* Visit the public link (e.g., `https://slide-controller.glitch.me`) to access your controller UI.

---

### 🧪 **Test It**

* Run your local `subscriber.py` script.
* Click **Next / Previous** in the web UI.
* The local machine should switch slides using `pyautogui`.

---

### 📁 **Glitch File Structure Overview**

```
/slide-controller (project root)
├── server.py           # Flask publisher
├── requirements.txt    # Python dependencies
├── index.html          # UI frontend
├── start.sh            # Start script
├── glitch.json         # Glitch config
├── .env                # MQTT credentials
```

---

### 💡 **Tips**

* Glitch auto-restarts the app when you edit files.
* You can share the public URL with any device for remote slide control.
* For better security, keep `.env` private (Glitch hides it from public views).


## 📌 License

This project is licensed under the MIT License.
Feel free to use and contribute!

---



