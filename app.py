import logging
import sys
import base64
import cv2
import numpy as np
import sqlite3
from flask import Flask, render_template, request, jsonify
from video_captioning import analyze_frame

# Suppress default Flask request logs
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)

app = Flask(__name__)

# Define alert keywords (Fix the missing comma)
ALERT_KEYWORDS = ["gun", "phone", "knife", "fire", "attack", "danger"]

@app.route('/')
def index():
    """Render the frontend page."""
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    """Receive and process a frame from the camera."""
    try:
        data = request.json['image']
        image_data = base64.b64decode(data.split(",")[1])
        nparr = np.frombuffer(image_data, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

        # Generate caption
        caption = analyze_frame(frame)

        # Debugging logs
        print(f"📌 Caption Processed: {caption}")
        print(f"🔍 Keywords List: {ALERT_KEYWORDS}")

        # Check if caption contains any alert words
        alert_triggered = any(keyword in caption.lower() for keyword in ALERT_KEYWORDS)

        if alert_triggered:
            logging.info(f"🚨 ALERT DETECTED: {caption}")

        response_data = {"caption": caption, "alert": alert_triggered}
        print(f"📤 Sending Response: {response_data}")

        return jsonify(response_data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

