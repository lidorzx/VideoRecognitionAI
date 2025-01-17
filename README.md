# First Create a Python environment
python -m venv video_recog
source video_recog/bin/activate
--------------------------------------
pip install -r requirements.txt
python app.py
static/styles.css - Defines the visual styling of the webpage
models/yolov8n.pt - Stores the YOLOv8 model file / you can edit the video captioning file and change the model. to bigger one.
templates/index.html - Displays the UI.
static/script.js - Captures frames, sends them to Flask, and updates captions dynamically.
app.py - Handles requests and serves the frontend.
video_captioning.py - Processes frames using YOLO and BLIP-2 models.

# for use of resources i decided to use the smallest one :
yolov8n.pt - quickest non accurate
yolov8s.pt - small less accurate
yolov8m.pt - medium fast
yolov8l.pt - large slow
yolov8x.pt - largest slowest

