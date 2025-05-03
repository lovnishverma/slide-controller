Here's a **project description** you can use for your **Slide Controller Web App using MQTT**:

---

## **Slide Controller – Remote Presentation Navigation via MQTT**

The **Slide Controller** is a responsive and user-friendly web application that allows seamless remote navigation of PowerPoint slides over MQTT. Designed for presenters, educators, and conference speakers, the app enables slide control through a web interface that communicates with a local Python MQTT subscriber script which simulates keyboard events to control slide transitions.

### ✅ **Key Features**

* **Beautiful Responsive UI**: Built with modern CSS design principles using cards, shadows, and clean typography.
* **Next/Previous Buttons**: Interactive control buttons to navigate presentation slides.
* **Live Status Indicator**: A real-time indicator shows MQTT connection status using color-coded visual cues.
* **Device Toggle & Sensitivity Slider**: Optional settings for gesture/trigger sensitivity (useful if extended for motion control).
* **Cross-Platform Web Access**: Works on desktop, tablets, and mobile browsers.
* **Integration Ready**: Easily extendable with gesture control, mobile sensors, or voice input.

### 🔧 **How It Works**

* The **Flask web app (hosted on Glitch)** acts as the **MQTT publisher**.
* The **Python script** on the local machine subscribes to MQTT topics and uses `pyautogui` to simulate keypresses (left/right arrows) for PowerPoint control.
* MQTT acts as the bridge between the remote web interface and the local machine running the presentation.

### 🧪 **Tech Stack**

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python (Flask), MQTT
* **MQTT Broker**: Public broker (e.g., `HiveMQ Cloud`) or local broker (e.g., Mosquitto)
* **Automation**: `pyautogui` for simulating key presses

### 📦 **Project Structure**

* `index.html` – Frontend interface for controlling slides
* `server.py` – Flask app to serve frontend and publish MQTT messages
* `subscriber.py` – Python MQTT client that receives commands and simulates keyboard input (run in host machine)

To convert your `subscriber.py` into a `.exe` file that you can run on any Windows system, you can use **PyInstaller**.

Here’s a **step-by-step guide** to create a `.exe` file:

---

### ✅ 1. **Install PyInstaller**

Open a terminal or command prompt and install PyInstaller:

```bash
pip install pyinstaller
```

---

### ✅ 2. **Navigate to your script directory**

```bash
cd path\to\your\script
```

Replace with the actual path where `subscriber.py` is saved.

---

### ✅ 3. **Create the .exe file**

Run:

```bash
pyinstaller --onefile subscriber.py
```

* `--onefile` generates a single `.exe` file.
* This creates a `dist` folder with `subscriber.exe` inside.

If you don't want the terminal window to show up when running the EXE (i.e., background script), add `--noconsole`:

```bash
pyinstaller --onefile --noconsole subscriber.py
```

---

### ✅ 4. **Run the EXE**

Navigate to:

```
dist\subscriber.exe
```

Double-click it. It will connect to the MQTT broker and wait for commands.

---

### ✅ Optional: Add an icon

If you want to add a custom icon:

```bash
pyinstaller --onefile --icon=your_icon.ico subscriber.py
```

---

### ⚠️ Important Notes

* Make sure the machine where you run the `.exe` has **PowerPoint installed and focused**.
* PyAutoGUI may require the script to run with admin privileges if you're interacting with certain windows.
* If packaging for another machine, ensure it has the same screen resolution and permissions.

You can create a `subscriber.spec` file if you want to customize the build further.

### 🚀 **Deployment**

* Flask app is deployed on **Glitch** for easy access and control from any device.
* Local subscriber script is run on the presentation computer, connected to the same MQTT broker.


