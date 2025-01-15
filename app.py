from flask import Flask, render_template, request, jsonify
from video_captioning import analyze_frame
import base64
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main page with the JavaScript controlled camera."""
    return render_template('index.html')

@app.route('/process_frame', methods=['POST'])
def process_frame():
    """Receive a frame from the client, process it, and return captions."""
    data = request.json['image']
    image_data = base64.b64decode(data.split(",")[1])
    nparr = np.frombuffer(image_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Process the frame and return captions
    caption = analyze_frame(frame)
    return jsonify({"caption": caption})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

