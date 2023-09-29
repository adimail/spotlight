document.addEventListener("DOMContentLoaded", function () {
    const chatMessages = document.getElementById("chat-messages");
    const userInput = document.getElementById("user-input");
    const sendButton = document.getElementById("send-button");

    sendButton.addEventListener("click", function () {
        const userMessage = userInput.value.trim();
        if (userMessage !== "") {
            appendMessage("You", userMessage);
            // You can send the userMessage to your backend or process it here
            userInput.value = "";
        }
    });

    function appendMessage(sender, message) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("message");

        const senderDiv = document.createElement("div");
        senderDiv.classList.add("message-sender");
        senderDiv.textContent = sender;

        const textDiv = document.createElement("div");
        textDiv.classList.add("message-text");
        textDiv.textContent = message;

        messageDiv.appendChild(senderDiv);
        messageDiv.appendChild(textDiv);

        chatMessages.appendChild(messageDiv);

        // Scroll to the bottom to show the latest message
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }
});
