import torch
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import cv2
import numpy as np
import re
import logging
import smtplib
from email.mime.text import MIMEText
from database import save_caption

# Load BLIP Model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Define alert keywords with word boundaries
ALERT_KEYWORDS = [r"\bphone\b", r"\bknife\b", r"\bweapon\b", r"\bfire\b", r"\bdanger\b", r"\battack\b"]

# Configure logging
logging.basicConfig(filename="alerts.log", level=logging.INFO, format="%(asctime)s - %(message)s")
alert_logger = logging.getLogger("alert_logger")

# Email Configuration
EMAIL_ALERTS_ENABLED = True  # Set to False to disable email alerts
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "mail."
EMAIL_PASSWORD = "pass"  # 🔴 Use the generated App Password
EMAIL_RECEIVER = "somemail."

def send_email_alert(caption):
    """Send an email alert when an alert keyword is detected."""
    if not EMAIL_ALERTS_ENABLED:
        print("📧 Email alerts are disabled.")  # Debugging step
        return

    subject = "⚠️ Security Alert: Suspicious Activity Detected"
    body = f"Alert Triggered: {caption}\nTimestamp: NOW"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    try:
        print(f"📧 Attempting to send email to {EMAIL_RECEIVER}...")  # Debugging step
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        server.quit()
        print(f"✅ Email sent successfully to {EMAIL_RECEIVER}")  # Debugging step
        logging.info(f"📧 Email alert sent: {caption}")
    except Exception as e:
        print(f"❌ Email sending failed: {e}")  # Debugging step
        logging.error(f"❌ Failed to send email: {e}")

def analyze_frame(frame):
    """Processes a frame, generates captions, and checks for alerts."""
    
    # Convert OpenCV frame to PIL Image
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # Generate Caption
    with torch.no_grad():
        inputs = processor(images=image, return_tensors="pt").to(device)
        outputs = model.generate(**inputs, max_length=50)
        caption = processor.decode(outputs[0], skip_special_tokens=True)

    print(f"📝 Generated Caption: {caption}")  # Debugging step

    # Check for alert conditions using regex
    alert_triggered = any(re.search(keyword, caption.lower()) for keyword in ALERT_KEYWORDS)

    if alert_triggered:
        print(f"🚨 ALERT MATCHED: {caption}")  # Debugging step
        logging.info(f"🚨 ALERT DETECTED: {caption}")
        send_email_alert(caption)  # 🚀 Send email when alert is detected

    # Save caption log in database
    save_caption(caption, int(alert_triggered))

    return caption

