const userInput = document.getElementById('user-input');
const sendButton = document.getElementById('send-button');
const messages = document.getElementById('messages');

sendButton.addEventListener('click', () => {
    const userInputValue = userInput.value.trim();
    if (userInputValue !== '') {
        const message = document.createElement('li');
        message.textContent = userInputValue;
        messages.appendChild(message);
        userInput.value = '';
        // Send the user input to the chatbot API
        fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ user_input: userInputValue })
        })
        .then(response => response.json())
        .then(data => {
            const chatbotResponse = data.response;
            const message = document.createElement('li');
            message.textContent = chatbotResponse;
            messages.appendChild(message);
        })
        .catch(error => console.error(error));
    }
});