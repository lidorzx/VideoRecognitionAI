# Video Recognition Application

This repository contains a web-based video recognition application leveraging YOLOv8 for object detection and BLIP-2 for video captioning. The application is designed for real-time frame analysis and caption generation.

---

## **Setup Instructions**

### **Step 1: Create a Python Environment**
1. Create a virtual environment:
   ```bash
   python -m venv video_recog
   source video_recog/bin/activate
   ```

### **Step 2: Install Dependencies**
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### **Step 3: Run the Application**
3. Start the application:
   ```bash
   python app.py
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

| Model          | Description                                |
|----------------|--------------------------------------------|
| `yolov8n.pt`   | Quickest, but least accurate.              |
| `yolov8s.pt`   | Small, fast, and less accurate.            |
| `yolov8m.pt`   | Medium, balances speed and accuracy.       |
| `yolov8l.pt`   | Large, more accurate but slower.           |
| `yolov8x.pt`   | Largest, most accurate, and slowest.       |

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

## **License**
This project is licensed under the MIT License.

---

### **Author**
Lidor Eliya

