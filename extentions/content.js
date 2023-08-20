var chatBox = document.createElement('div');
chatBox.id = 'chat-box';
document.body.appendChild(chatBox);

var chatLog = document.createElement('textarea');
chatLog.id = 'chat-log';
chatLog.readOnly = true;
chatBox.appendChild(chatLog);

var chatInput = document.createElement('input');
chatInput.id = 'chat-input';
chatInput.type = 'text';
chatBox.appendChild(chatInput);

var sendButton = document.createElement('button');
sendButton.id = 'send-button';
sendButton.textContent = '보내기';
sendButton.onclick = sendMessage;
chatBox.appendChild(sendButton);

function sendMessage() {
  chatLog.value += "나: " + chatInput.value + "\n";
  // 챗봇 응답 로직
  chatLog.value += "챗봇: 안녕하세요!\n"; // 예시 응답
  chatInput.value = '';
}
