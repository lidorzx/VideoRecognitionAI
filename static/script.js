document.addEventListener("DOMContentLoaded", async function () {
    const videoElement = document.getElementById('cameraFeed');
    const captionText = document.getElementById('captionText');
    const errorMessage = document.getElementById('error-message');

    // Start the camera feed
    async function startCamera() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoElement.srcObject = stream;
            console.log("✅ Camera access granted.");
            sendFramesToServer(videoElement);
        } catch (error) {
            errorMessage.textContent = "Camera access error: " + error.message;
        }
    }

    // Send frames to the Flask server every 1 second for analysis
    async function sendFramesToServer(videoElement) {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');

        setInterval(async () => {
            canvas.width = videoElement.videoWidth;
            canvas.height = videoElement.videoHeight;
            context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

            const imageData = canvas.toDataURL('image/jpeg');

            try {
                const response = await fetch('/process_frame', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ image: imageData })
                });

                const result = await response.json();
                captionText.innerText = `Caption: ${result.caption}`;
            } catch (error) {
                console.error("❌ Error sending frames:", error);
            }
        }, 1000); // Sends a frame every second
    }

    // Start the camera feed when the page loads
    startCamera();
});

