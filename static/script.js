document.addEventListener("DOMContentLoaded", async function () {
    const videoElement = document.getElementById('cameraFeed');
    const captionText = document.getElementById('captionText');
    const errorMessage = document.getElementById('error-message');
    const speedControl = document.getElementById('speedControl');
    const speedValue = document.getElementById('speedValue');

    let captureInterval = 3000;  // Default interval set to 5 seconds

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

    // Function to send frames to the Flask server
    function sendFramesToServer(videoElement) {
        const canvas = document.createElement('canvas');
        const context = canvas.getContext('2d');

        function captureFrame() {
            canvas.width = videoElement.videoWidth;
            canvas.height = videoElement.videoHeight;
            context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

            const imageData = canvas.toDataURL('image/jpeg');

            fetch('/process_frame', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ image: imageData })
            })
            .then(response => response.json())
            .then(result => {
                captionText.innerText = `Caption: ${result.caption}`;
            })
            .catch(error => {
                console.error("❌ Error sending frames:", error);
            });
        }

        // Start the interval with the default delay
        let intervalID = setInterval(captureFrame, captureInterval);

        // Event listener for speed control input (dynamically change interval)
        speedControl.addEventListener('input', function () {
            clearInterval(intervalID);
            captureInterval = parseInt(speedControl.value);
            speedValue.innerText = `${captureInterval / 1000} seconds`;
            intervalID = setInterval(captureFrame, captureInterval);
        });
    }

    // Start the camera feed when the page loads
    startCamera();
});

