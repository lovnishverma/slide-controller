![slide-controller](https://github.com/user-attachments/assets/5e1088ee-0f61-4086-9516-6475d13f5f83)


### **Slide Controller: Revolutionizing Remote Presentation Control with MQTT**  
**Created by Lovnish Verma**  

Tired of relying on expensive proprietary devices like the **[Logitech Wireless Presenter R400](https://amzn.in/d/hJ9VZkL), etc** to control your slides? Meet **Slide Controller**—a cutting-edge, open-source web application that turns your smartphone, tablet, or laptop into a **fully customizable, feature-rich presentation remote**—all for **FREE**!  

---

### **Why Slide Controller is Revolutionary?**  
1️⃣ **No Hardware Required**  
   - Forget physical presenters. Use **any internet-connected device** as your remote control. Works on **mobile, tablet, or desktop browsers**.  

2️⃣ **MQTT-Powered Connectivity**  
   - Leverages **MQTT**, the industry-standard IoT protocol, for **real-time, low-latency slide transitions**. Unlike traditional remotes, it’s **extendable** to integrate with IoT devices, voice assistants, or even custom hardware.  

3️⃣ **Motion & Gesture Control**  
   - **Shake your device** to skip slides or adjust sensitivity via a built-in slider. No need to press buttons—your movements become commands!  

4️⃣ **Haptic Feedback**  
   - Feel vibrations on your device when slides change, ensuring you’re always in sync with your presentation.  

5️⃣ **Cross-Platform & Open-Source**  
   - Fully customizable codebase. Tweak UI/UX, add new features (like voice commands or gesture recognition), or integrate it with smart devices—**the possibilities are endless**!  

6️⃣ **Dark Mode & Responsive Design**  
   - A sleek, **modern UI** with toggleable dark mode and pixel-perfect responsiveness for **every screen size**.  

---

### **How It Works**  
- **Web Interface**: Hosted on platforms like **Glitch**, the frontend provides intuitive controls.  
- **MQTT Broker**: Uses **HiveMQ Cloud** or local brokers (like Mosquitto) for reliable communication.  
- **Local Automation**: A Python script listens to MQTT messages and uses **`pyautogui`** to simulate keyboard inputs, controlling PowerPoint directly.  

---

### **Features That Set It Apart**  
| **Unique Features** | **Traditional Remotes** | **Slide Controller** |  
|----------------------|-------------------------|----------------------|  
| **Cost**             | ₹2,500+                | **FREE** (Open Source)|  
| **Customization**    | Limited buttons         | Add voice/gesture/IoT controls |  
| **Connectivity**     | Wired/Wi-Fi only        | Cross-platform via MQTT |  
| **Feedback**         | None                    | Haptic vibrations + visual cues |  
| **Extensibility**    | Closed ecosystem        | Fully open-source, hackable |  

---

### **Technical Highlights**  
- **Stack**: HTML/CSS/JS for the frontend, **Python Flask** + **Paho MQTT** for backend, and **PyAutoGUI** for automation.  
- **Deployment**: Host the web app on **Glitch** in minutes—no server setup required.  
- **Security**: Uses secure MQTT brokers like **HiveMQ Cloud** with TLS encryption.  
- **Accessibility**: Works offline (for motion controls) and supports **keyboard shortcuts** for touch-free operation.  

---

### **Use Cases**  
- **Educators**: Control slides while moving around the classroom.  
- **Speakers**: Eliminate the hassle of carrying physical remotes.  
- **Hackathon Projects**: Extend it with **Arduino/ESP32** for custom hardware controllers.  
- **Conference Setup**: Manage multiple presentations from a single browser tab.  

---

### **What Makes It Truly Unique?**  
- **First-of-Its-Kind Integration**: Combines **motion sensing**, **MQTT**, and **web automation** into a single package.  
- **Zero Setup Hassle**: No dongles, no pairing—just open the web app and start controlling.  
- **Community-Driven**: Open-source code means continuous improvements and new features from contributors worldwide.  

---

### **"This isn’t just a remote—it’s a platform for innovation!"**  

---

### **Ready to Ditch Expensive Hardware?**  
**Slide Controller** redefines presentation control by merging modern web technologies with IoT principles. With its **cost-effectiveness**, **versatility**, and **endless customization options**, it’s the future of slide navigation.  

👉 **Deploy your own instance in 5 minutes**: [GitHub Repo](https://github.com/lovnishverma/slide-controller)  
👉 **Live Demo**: [https://remotecontroller.glitch.me](https://remotecontroller.glitch.me)  

---

**Join the revolution** and make your presentations smarter, cheaper, and infinitely more powerful!  

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

1. **Frontend (templates/index.html)**: Web UI hosted on **Glitch.com** acts as the **MQTT publisher**.
2. **Backend (server.py)**: Flask app serves the frontend and publishes MQTT messages. Hosted on **Glitch.com**
3. **Local Subscriber (subscriber.py)**: Listens to MQTT messages and uses `pyautogui` to simulate PowerPoint key presses.

## 🧰 Tech Stack

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python (Flask), Paho MQTT
* **MQTT Broker**: [HiveMQ Cloud](https://console.hivemq.cloud/), Mosquitto (local), or Adafruit IO
* **Automation**: `pyautogui` for keyboard simulation

---

## 📁 Project Structure

```
slide-controller/
├── templates/index.html          # Web UI
├── server.py           # Flask MQTT publisher
├── subscriber.py       # Python MQTT subscriber (run in local machine host machine)
└── subscriber.exe    # Optional EXE file that you can run on windows pc
```

---

## 🔄 Running the App

### 1. 🚀 Open Control Website deployed on glitch.me

```markdown
🚀 **Live Demo**: [https://remotecontroller.glitch.me](https://remotecontroller.glitch.me)
```

---

### 2. 💻 Run Subscriber Script or convert script to .exe file then run that...

To install **PyInstaller**, run the following command in your terminal:

```bash
pip install pyinstaller
```

This will install the latest version of PyInstaller, which allows you to bundle your Python script into a standalone executable for your operating system.

### To verify installation:

```bash
pyinstaller --version
```

### Basic usage to convert your script to an executable:

```bash
pyinstaller --onefile subscriber.py
```

This will create a `dist/subscriber` (or `.exe` on Windows) binary **you can run without needing Python installed.**


To Convert `subscriber.py` to `.exe` with icon using PyInstaller:

**Note:** To generate icon go to https://www.icoconverter.com/ upload .jpg or .png  and get your icon in .ico format

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

### ⚙️ Option 2: Use Local Mosquitto Broker (for advanced users only)

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
* Web UI (flask app) can be hosted on pythonanywhere.com or Glitch.com.

---

## 📸 Screenshots

 **Slide Controller Flask App using MQTT**
Web UI Running on android or ios phone to control host machine:
![image](https://github.com/user-attachments/assets/24111d5c-0497-42dc-aaab-ec9ba812dbf8)

 **Subscribe.exe running on Host Machine**

![image](https://github.com/user-attachments/assets/a2d327c5-0461-457e-8442-c6b9d678527c)

---

![346560f29b3e06f6ee0c598868a3e9cef7314c59](https://github.com/user-attachments/assets/f83b68ce-e3cd-4a22-97fe-55db855ae51b)


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
├── templates/index.html          # UI frontend
├── start.sh            # Start script
├── glitch.json         # Glitch config
├── .env                # MQTT credentials
```

---

### 💡 **Tips**

* Glitch auto-restarts the app when you edit files.
* You can share the public URL with any device for remote slide control.
* For better security, keep `.env` private (Glitch hides it from public views).


---

### 💡 **Future Works**

* **Add User Authentication**
  Implement login functionality to restrict access to the slide controller. This will enhance security, especially when the app is publicly hosted.

* **Build Dedicated Hardware Using ESP8266**
  Design and deploy a custom physical slide controller using an ESP8266 microcontroller with pushbuttons. This device will connect to the MQTT broker and allow presenters to control slides wirelessly and independently of a smartphone or PC.

---

Note: I'm Working a circuit diagram and Arduino code for the ESP8266-based pushbutton controller

---


#### 1. **GitHub Repository Link (available)**

If you’re sharing this online:

```markdown
🔗 [View on GitHub](https://github.com/lovnishverma/slide-controller)
```

---

#### 2. **Live Demo Section (On Glitch)**

If the Glitch deployment is public:

```markdown
🚀 **Live Demo**: [https://remotecontroller.glitch.me](https://remotecontroller.glitch.me)
```

---

#### 3. **Libraries `requirements.txt` for Host Machine**

Here's the `requirements.txt` for your `subscriber.py` script: Install in Local PC
The dependencies to install:

```txt
paho-mqtt
pyautogui
pyinstaller
```

Create requirements.txt and add above libraries in it then enter command:

```bash
pip install -r requirements.txt
```

---

#### 4. **Enhance Security Note for HiveMQ**

> 🔐 **Security Tip**: Avoid hardcoding sensitive credentials in code. Use environment variables (`os.environ.get()`) or a `.env` file with `python-dotenv` package.

---

#### 5. **EXE Use Case**

Note: `subscriber.exe` is only needed on the system running PowerPoint.

---

#### 6. **Developer Notes or Customization Ideas**

My Fellow Developers let's developers extend it:

```markdown
### 🧩 Developer Notes

* Add swipe detection with JavaScript for touch devices.
* Integrate voice control via Web Speech API.
* Use ESP8266 + accelerometer for physical gesture-based control.
```

---

### 7. 📌 License

This project is licensed under the MIT License.
Feel free to use and contribute!


---

#### 8. **MQTT Troubleshooting Tips**

Just in case:

```markdown
### 🧰 MQTT Troubleshooting

* Check broker connectivity (try with `mosquitto_sub` and `mosquitto_pub`).
* Verify correct topic and credentials.
* Ensure `subscriber.py` has access to the screen.
* Use `client.on_log()` to debug MQTT activity.
```

---

#### 9. **Contribution Guidelines**

Please do contribute:

```markdown
## 🤝 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/cool-feature`)
3. Commit your changes (`git commit -am 'Add cool feature'`)
4. Push to the branch (`git push origin feature/cool-feature`)
5. Open a Pull Request
```

---
