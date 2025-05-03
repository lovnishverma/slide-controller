Sure! Here's the full **Glitch Deployment Guide** continuation for your **Slide Controller Flask App**:

---

### 3️⃣ **Delete Existing Files**

Once inside the `slide-controller` project:

1. Delete all default files:

   * `server.js`
   * `package.json`
   * `.env`, etc.

> You can do this from the **“Files” sidebar** (click the 3 dots beside each file).

---

### 4️⃣ **Add Your Python Files**

Now upload your Python Flask app files:

1. Click **“New File”** and add:

   * `server.py`
   * `requirements.txt`
   * Folder `templates/` → Inside it, add `index.html`

Your Glitch project structure should now look like:

```
slide-controller/
├── server.py
├── requirements.txt
└── templates/
    └── index.html
```

---

### 5️⃣ **Add Required Packages**

Create a file called `requirements.txt` with:

```txt
Flask==2.3.3
paho-mqtt==1.6.1
```

Make sure this file is saved.

---

### 6️⃣ **Enable Glitch's Python Runtime**

Glitch projects are Node.js by default, but you can configure Python:

1. Create a new file called `.glitch-assets` (can be empty — it just helps keep Python active).
2. Click the **“Tools” > “Terminal”** in Glitch’s sidebar.
3. In the terminal, type:

```bash
echo "python3 server.py" > start.sh
chmod +x start.sh
```

This will create a `start.sh` script to run your Flask app.

---

### 7️⃣ **Create a `glitch.json` File**

To tell Glitch how to run your app, create a file called `glitch.json`:

```json
{
  "install": "pip3 install -r requirements.txt",
  "start": "bash start.sh"
}
```

---

### 8️⃣ **Modify `server.py` for Glitch Hosting**

Make sure `server.py` uses:

```python
app.run(host='0.0.0.0', port=3000)
```

This is required for Glitch to expose your app publicly.

---

### 9️⃣ **Start the App**

Glitch will auto-install dependencies and run the server.

* Once live, your app will be available at:

  ```
  https://<your-project-name>.glitch.me
  ```

You can now access the Slide Controller interface from any device browser!

---

## 🔒 Notes on Using HiveMQ Cloud with Glitch

If you're using a **secure MQTT broker** like HiveMQ:

* Ensure the TLS port (`8883`) is used.
* If Glitch fails to connect due to SSL, try a public unsecured broker (e.g., `test.mosquitto.org`) temporarily for testing.

You may also consider switching to **WebSockets MQTT** (e.g., `mqtts://`) for full browser compatibility in future enhancements.

---

## 🧼 Cleanup Tips

* Glitch automatically wakes your project when visited and sleeps after inactivity.
* Upgrade to Glitch Pro for persistent uptime and private code.

---

## ✅ You're Done!

🔗 This Project in Open For Contributions
