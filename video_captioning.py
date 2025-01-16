import cv2
from ultralytics import YOLO
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

# Load YOLOv8 and BLIP-2 models
model = YOLO('models/yolov8n.pt')
blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large").to("cuda" if torch.cuda.is_available() else "cpu")

def analyze_frame(frame):
    """Analyze the frame using YOLO and BLIP-2 and return captions."""
    # YOLOv8 object detection
    results = model(frame)[0]  # Access the first element in the list directly
    detected_objects = []

    # Access results correctly
    for box in results.boxes.data.tolist():  # Ensure accessing the data correctly
        x1, y1, x2, y2, conf, cls = box
        label = f"{model.names[int(cls)]} ({conf:.2f})"
        detected_objects.append(label)

    # BLIP-2 captioning
    inputs = blip_processor(frame, return_tensors="pt").to("cuda" if torch.cuda.is_available() else "cpu")
    captions = blip_model.generate(inputs["pixel_values"])
    caption_text = blip_processor.batch_decode(captions, skip_special_tokens=True)[0]

    # Return combined caption and detections
    return f"Detected: {', '.join(detected_objects)} | Caption: {caption_text}"

