import logging
import sys

# Suppress default Flask request logs
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

# Prevent Flask logs from going to the alerts.log
logging.getLogger("werkzeug").addHandler(logging.StreamHandler(sys.stdout))

from flask import Flask, render_template, request, jsonify
from video_captioning import analyze_frame
import base64
import cv2
import numpy as np
import sqlite3
import logging

app = Flask(__name__)

# Define alert keywords (modify as needed)
ALERT_KEYWORDS = ["phone", "cell", "knife", "firearm", "danger"]

# Configure logging
logging.basicConfig(filename="alerts.log", level=logging.INFO, format="%(asctime)s - %(message)s")

def check_for_alert(caption):
    """Check if caption contains alert keywords."""
    return any(keyword in caption.lower() for keyword in ALERT_KEYWORDS)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    """Receive and process a frame, log captions, and trigger alerts."""
    data = request.json['image']
    image_data = base64.b64decode(data.split(",")[1])
    nparr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Generate caption
    caption = analyze_frame(frame)

    # Check for alert keywords
    alert_triggered = 1 if check_for_alert(caption) else 0

    # Save caption to database
    conn = sqlite3.connect("captions.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO captions (caption, alert_triggered) VALUES (?, ?)", (caption, alert_triggered))
    conn.commit()
    conn.close()

    # Log alert if triggered
    if alert_triggered:
        logging.info(f"⚠️ ALERT DETECTED: {caption}")

    return jsonify({"caption": caption, "alert": bool(alert_triggered)})

@app.route('/logs', methods=['GET'])
def get_logs():
    """Fetch recent caption logs."""
    conn = sqlite3.connect("captions.db")
    cursor = conn.cursor()
    cursor.execute("SELECT timestamp, caption, alert_triggered FROM captions ORDER BY timestamp DESC LIMIT 50")
    logs = [{"timestamp": row[0], "caption": row[1], "alert": bool(row[2])} for row in cursor.fetchall()]
    conn.close()

    return jsonify(logs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

