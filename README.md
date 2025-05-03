```markdown
# 🚀 Slide Controller – Remote Presentation Navigation via MQTT

The **Slide Controller** is a responsive and user-friendly web application that allows seamless **remote navigation of PowerPoint slides over MQTT**. Designed for **presenters, educators, and conference speakers**, the app enables slide control through a web interface that communicates with a local Python MQTT subscriber script which simulates keyboard events to control slide transitions.

## ✅ Key Features
- 🎨 **Beautiful Responsive UI**: Modern CSS design with cards, shadows, and clean typography.
- ⏭️ **Next/Previous Buttons**: Navigate presentation slides interactively.
- 🟢 **Live Status Indicator**: Real-time MQTT connection status with color-coded indicators.
- 🎛️ **Device Toggle & Sensitivity Slider**: Optional controls for motion/gesture extensions.
- 🌐 **Cross-Platform Access**: Works on mobile, tablet, and desktop browsers.
- 🔌 **Integration Ready**: Extendable for gesture, voice, or IoT triggers.
- 📲 **Vibration Feedback**: Haptic feedback on slide changes and motion detection.
- 🌑 **Dark Mode**: Toggleable dark mode for better visibility in low-light conditions.

## 🛠️ How It Works
1. **Frontend (templates/index.html)**: Web UI hosted on **Glitch** acts as the **MQTT publisher**. (deployed on glitch.com)
2. **Backend (server.py)**: Flask app serves the frontend and publishes MQTT messages. (deployed on glitch.com)
3. **Local Subscriber (subscriber.py or subscriber.exe)**: Listens to MQTT messages and uses `pyautogui` to simulate PowerPoint key presses.

## 🧰 Tech Stack
- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask), Paho MQTT
- **MQTT Broker**: [HiveMQ Cloud](https://console.hivemq.cloud/), Mosquitto (local), or Adafruit IO
- **Automation**: `pyautogui` for keyboard simulation

## 📁 Project Structure
```
slide-controller/
├── templates/
│   └── index.html          # Web UI
├── server.py               # Flask MQTT publisher
├── subscriber.py           # Python MQTT subscriber (run in local machine/host machine)
├── subscriber.exe          # Optional EXE file that you can run on Windows PC
├── requirements.txt        # Python dependencies
├── start.sh                # Start script for Glitch
├── glitch.json             # Glitch configuration
├── .env                    # MQTT credentials (keep private)
├── README.md               # Project documentation
```

## 🔄 Running the App

### 1. 🚀 Open Control Website Deployed on Glitch
Visit the live demo:
[https://remotecontroller.glitch.me](https://remotecontroller.glitch.me)

### 2. 💻 Run Subscriber Script
Ensure you have Python installed on your system.

#### Option A: Run Directly from Source
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Script**:
   ```bash
   python subscriber.py
   ```

#### Option B: Convert Script to .exe File (Windows)
1. **Install PyInstaller**:
   ```bash
   pip install pyinstaller
   ```
To genreate .ico icon from .png pr .jpg go to https://www.icoconverter.com/

2. **Generate .exe File**:
   ```bash
   pyinstaller --onefile --icon=slidecontrol.ico subscriber.py
   ```
   Or, if you want to hide the console:
   ```bash
   pyinstaller --onefile --noconsole --icon=slidecontrol.ico subscriber.py
   ```

3. **Run the .exe File**:
   ```bash
   dist\subscriber.exe
   ```

## 🌐 Set Up MQTT Broker

### ✅ Option 1: Use HiveMQ Cloud (Recommended)
> HiveMQ Cloud is free, secure, reliable, and requires no local setup.

#### 🔐 Step-by-Step: Create a HiveMQ Cloud Broker
1. **Go to HiveMQ Cloud**:
   [https://console.hivemq.cloud/](https://console.hivemq.cloud/)

2. **Sign Up / Log In**:
   - Create a free account or log in.

3. **Create a New Cluster**:
   - Click **"Create New Cluster"**
   - Choose **Free Tier**
   - Name your cluster (e.g., `slide-controller`)
   - Wait 1–2 minutes for provisioning.

4. **View Connection Details**:
   - Once cluster is ready, click **"View Connection Details"**
   - Note the **Broker Hostname** and **Port** (`8883` for TLS)

5. **Create MQTT Credentials**:
   - Go to **Access Management > Credentials**
   - Click **Create New Credential**
     - Choose a **Username** (e.g., `slideuser`)
     - Set a **Password** (e.g., `myslidesecret`)
   - Save these for your `server.py` and `subscriber.py`

6. **Enable TLS/SSL** (Optional but recommended):
   - HiveMQ Cloud requires TLS (port 8883)
   - You must install `paho-mqtt` with TLS support:
     ```bash
     pip install paho-mqtt
     ```

#### ✅ Example HiveMQ Configuration
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

### ✅ Option 2: Use Local Mosquitto Broker
#### Install on Windows/Linux:
```bash
sudo apt install mosquitto mosquitto-clients
```

Start broker:
```bash
mosquitto
```

Set `BROKER = "localhost"` and `PORT = 1883` in your scripts.

## 🧪 Test It Out
- Open your Flask web app in a browser.
- Click "Next" or "Previous" buttons.
- On the presentation computer, ensure `subscriber.exe` is running and PowerPoint is focused.
- Slide transitions should occur instantly.

## 📝 Notes
- You can add gestures, voice, or phone sensors to enhance control.
- Ensure subscriber script runs with proper screen access.
- Web UI can be hosted on any static site host or Glitch.

## 📸 Screenshots


![image](https://github.com/user-attachments/assets/24111d5c-0497-42dc-aaab-ec9ba812dbf8)


![image](https://github.com/user-attachments/assets/a2d327c5-0461-457e-8442-c6b9d678527c)


## 🚀 **Glitch Deployment Guide – Slide Controller Web App**

This guide walks you through **hosting the Flask MQTT Publisher (Web App)** on **Glitch.com**, a free online IDE and hosting platform ideal for quick web app deployment and sharing.

### 🔧 **What You’ll Deploy**
You’ll host the `server.py` Flask app (MQTT Publisher) along with its frontend (`index.html`) on Glitch. The app will expose a public URL (e.g., `https://slide-controller.glitch.me`) that can send MQTT messages to your local subscriber script.

### ✅ **Step-by-Step Deployment on Glitch**

#### 1️⃣ **Sign Up or Log In**
- Visit: [https://glitch.com/](https://glitch.com/)
- Click **Sign Up** or **Log In** using GitHub, Google, or email.

#### 2️⃣ **Create a New Project**
- Click **“New Project” → “Hello-Express”** (Glitch supports Node.js by default).
- Rename the project to something like `slide-controller`.

#### 3️⃣ **Delete Existing Files**
Delete these default files from Glitch:
- `server.js`
- `package.json`
- `public/`
- `views/`

#### 4️⃣ **Add Your Flask App Files**
Upload or manually create the following files:
- `server.py` – Your Flask MQTT Publisher code
- `requirements.txt` – Add this content:
  ```txt
  Flask
  paho-mqtt
  ```
- `templates/index.html` – Your frontend controller page
- `start.sh` – A custom shell script to launch your Flask app
- `glitch.json` – Glitch configuration
- `.env` – MQTT credentials (keep private)

#### Example `start.sh` Content:
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

#### Example `glitch.json` Content:
```json
{
  "start": "bash start.sh"
}
```

#### Example `.env` Content:
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

#### 5️⃣ **Start the App**
Once files are ready:
- Click the **“Logs”** button to see output.
- Glitch will auto-run `start.sh`.
- Visit the public link (e.g., `https://slide-controller.glitch.me`) to access your controller UI.

### 🧪 **Test It**
- Run your local `subscriber.py` script.
- Click **Next / Previous** in the web UI.
- The local machine should switch slides using `pyautogui`.

## 🧩 Developer Notes
- **Add Swipe Detection**: Implement swipe detection with JavaScript for touch devices.
- **Integrate Voice Control**: Use Web Speech API for voice commands.
- **Physical Gesture Control**: Use ESP8266 + accelerometer for physical gesture-based control.

## 🔒 Security Tips
- **Environment Variables**: Avoid hardcoding sensitive credentials in code. Use environment variables (`os.environ.get()`) or a `.env` file with `python-dotenv` package.
- **MQTT Broker Security**: Ensure your MQTT broker is secure, especially if using a public cloud service.

## 📌 License
This project is licensed under the MIT License. Feel free to use and contribute!

## 🧰 MQTT Troubleshooting
- **Check Broker Connectivity**: Try with `mosquitto_sub` and `mosquitto_pub`.
- **Verify Correct Topic and Credentials**: Ensure topics match and credentials are correct.
- **Screen Access**: Ensure `subscriber.py` has access to the screen.
- **Debug MQTT Activity**: Use `client.on_log()` to debug MQTT activity.

## 🤝 Contributing
1. Fork the repo
2. Create your feature branch (`git checkout -b feature/cool-feature`)
3. Commit your changes (`git commit -am 'Add cool feature'`)
4. Push to the branch (`git push origin feature/cool-feature`)
5. Open a Pull Request

## 📚 Resources
- [HiveMQ Cloud Documentation](https://www.hivemq.com/docs/cloud/introduction/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Paho MQTT Documentation](https://www.eclipse.org/paho/index.php?page=clients/python/docs/index.php)
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/en/latest/)

## 📞 Contact
For any questions or support, feel free to reach out:
- **Email**: [your-email@example.com](mailto:princelv84@gmail.com)
- **GitHub**: [lovnishverma](https://github.com/lovnishverma)

---

**Enjoy controlling your presentations remotely with Slide Controller!**
```

### Key Sections:
1. **Introduction**: Brief overview of the project.
2. **Key Features**: Highlight the main features of the application.
3. **How It Works**: Explanation of the architecture and flow.
4. **Tech Stack**: List of technologies used.
5. **Project Structure**: Overview of the directory structure.
6. **Running the App**: Instructions for setting up and running the application.
7. **MQTT Broker Setup**: Detailed steps for setting up an MQTT broker using HiveMQ Cloud or a local Mosquitto broker.
8. **Testing**: Steps to test the application.
9. **Notes**: Additional tips and considerations.
10. **Screenshots**: Visual representation of the application.
11. **Glitch Deployment Guide**: Detailed instructions for deploying the Flask app on Glitch.
12. **Developer Notes**: Ideas for extending the application.
13. **Security Tips**: Best practices for securing the application.
14. **License**: Licensing information.
15. **MQTT Troubleshooting**: Common issues and solutions.
16. **Contributing**: Guidelines for contributing to the project.
17. **Resources**: Links to relevant documentation.
18. **Contact**: Contact information for support and inquiries.
