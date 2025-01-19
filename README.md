# Video Recognition Application
![image](https://github.com/user-attachments/assets/cdd383de-1711-453f-9444-0bfa88bcda6f)


This repository contains a web-based video recognition application leveraging YOLOv8 for object detection and BLIP-2 for video captioning. The application is designed for real-time frame analysis and caption generation.

---

## **Setup Instructions**

### **Step 1: Clone the Repository**

1. Clone the repository:
   ```bash
   git clone https://github.com/lidorzx/VideoRecognitionAI.git
   ```

2. Navigate into the directory:
   ```bash
   cd VideoRecognitionAI
   ```

### **Step 2: Create a Python Environment**

3. Create a virtual environment:
   ```bash
   python -m venv videorecognitionai
   source videorecognitionai/bin/activate
   ```

### **Step 3: Install Dependencies**

4. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### **Step 4: Run the Application**

5. Start the application:
   ```bash
   python app.py
   ```
### **Possible: Using Docker**
   ```bash
 Build the Image  : docker build -t video_recognition:latest .
 Run the Container : docker run -p 5000:5000 video_recognition:latest
   ```

### Possible: Using Docker Compose 

 Using Docker-Compose
   ```bash
   docker compose up
   ```
---

## **File Structure**

### **Backend**

- **`app.py`**: The core of the application, responsible for handling requests, processing video frames, and serving the frontend.
- **`video_captioning.py`**: Handles frame processing using YOLO and BLIP-2 models.

### **Frontend**

- **`templates/index.html`**: Defines the structure of the user interface.
- **`static/styles.css`**: Contains styles for the webpage to ensure a clean, professional look.
- **`static/script.js`**: Captures video frames, communicates with Flask, and dynamically updates captions on the webpage.

### **Models**

- **`models/yolov8n.pt`**: The YOLOv8 model file for object detection. Replace this file with a different model to adjust accuracy and speed.

---

## **YOLOv8 Models**

You can select from various YOLOv8 models based on your resource requirements and performance needs:

| Model        | Description                          | Download Link |
| ------------ | ------------------------------------ | ------------- |
| `yolov8n.pt` | Quickest, but least accurate.        | [Download](https://huggingface.co/Ultralytics/YOLOv8/blob/main/yolov8n.pt) |
| `yolov8s.pt` | Small, fast, and less accurate.      | [Download](https://huggingface.co/Ultralytics/YOLOv8/blob/main/yolov8s.pt) |
| `yolov8m.pt` | Medium, balances speed and accuracy. | [Download](https://huggingface.co/Ultralytics/YOLOv8/blob/main/yolov8m.pt) |
| `yolov8l.pt` | Large, more accurate but slower.     | [Download](https://huggingface.co/Ultralytics/YOLOv8/blob/main/yolov8l.pt) |
| `yolov8x.pt` | Largest, most accurate, and slowest. | [Download](https://huggingface.co/Ultralytics/YOLOv8/blob/main/yolov8x.pt) |

To change the model, replace `models/yolov8n.pt` with the desired model file.

---

## **How It Works**

1. **Video Frames**: Frames are captured from the video and sent to the backend via JavaScript.
2. **YOLOv8 Model**: The frames are processed using the selected YOLOv8 model for object detection.
3. **BLIP-2 Model**: Captions are generated for detected objects in the frames.
4. **Dynamic Updates**: Results are sent back to the frontend and displayed in real-time.

---

## **Customize the Application**

### **Styling**

Modify `static/styles.css` to change the appearance of the webpage.

### **Frontend Behavior**

Edit `static/script.js` to adjust frame capturing or add new dynamic features.

### **Backend Logic**

Update `app.py` and `video_captioning.py` to customize frame processing or integrate additional models.

---

## **Contributing**

We welcome contributions! Feel free to submit issues or pull requests to improve the application.

---

## **Tags**

- `video-recognition`
- `object-detection`
- `YOLOv8`
- `real-time-processing`
- `BLIP-2`
- `machine-learning`
- `AI`
- `deep-learning`
- `python`
- `open-source`

---

### **Author**

Lidor Eliya

