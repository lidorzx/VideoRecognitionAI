document.addEventListener("DOMContentLoaded", async function () {
    const videoElement = document.getElementById("cameraFeed");
    const captionText = document.getElementById("captionText");
    const alertsContainer = document.getElementById("alerts");

    async function startCamera() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });
            videoElement.srcObject = stream;
            console.log("✅ Camera access granted.");
            sendFramesToServer();
        } catch (error) {
            console.error("❌ Camera access error:", error);
            alert("Failed to access camera. Check permissions.");
        }
    }

    function sendFramesToServer() {
        const canvas = document.createElement("canvas");
        const context = canvas.getContext("2d");

        setInterval(async () => {
            canvas.width = videoElement.videoWidth;
            canvas.height = videoElement.videoHeight;
            context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);

            const imageData = canvas.toDataURL("image/jpeg");

            try {
                const response = await fetch("/process_frame", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ image: imageData })
                });

                const result = await response.json();

                console.log("📌 Caption from Flask:", result.caption);
                console.log("🚨 Alert Status from Flask:", result.alert);

                updateCaption(result.caption);

                if (result.alert === true) {  // Ensure it's read as boolean
                    displayAlert(result.caption);
                } else {
                    clearAlerts();
                }
            } catch (error) {
                console.error("❌ Error sending frames:", error);
            }
        }, 2000);
    }

    function updateCaption(text) {
        captionText.innerText = text;
    }

    function displayAlert(caption) {
        console.log("⚠️ Displaying Alert in UI:", caption);

        alertsContainer.innerHTML = ""; // Clear previous alerts

        const alertMessage = document.createElement("p");
        alertMessage.classList.add("alert-message");
        alertMessage.innerText = `⚠️ ALERT: ${caption}`;

        alertsContainer.appendChild(alertMessage);

        // Remove alert after 8 seconds
        setTimeout(() => {
            alertMessage.style.opacity = "0";
            setTimeout(() => alertMessage.remove(), 1000);
        }, 7000);
    }

    function clearAlerts() {
        console.log("✅ No Alert - Clearing UI");
        alertsContainer.innerHTML = "<p>No alerts detected.</p>";
    }

    startCamera();
});

