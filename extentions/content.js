const chatbotHTML = `
  <div id="chatbot" class="chatbot">
    <img src="chatbot_icon.png" id="chatbot-icon" class="chatbot-icon" alt="Chatbot">
    <div class="chat-window" style="display:none;">
      <div class="messages"></div>
      <input type="text" class="user-input" placeholder="메시지 입력"/>
    </div>
  </div>`;

document.body.insertAdjacentHTML('beforeend', chatbotHTML);

const chatbotIcon = document.getElementById('chatbot-icon');
const chatWindow = document.querySelector('.chat-window');

chatbotIcon.addEventListener('click', () => {
  chatWindow.style.display = chatWindow.style.display === 'none' ? 'block' : 'none';
});
