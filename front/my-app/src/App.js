import React, { useState, useRef, useEffect } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import chatbotImage from './logo.png'; // 챗봇 이미지를 추가하세요.

function App() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);
  const chatRef = useRef(null);

  const handleSend = () => {
    setChat([...chat, message]);
    setMessage('');
  };

  useEffect(() => {
    if (chatRef.current) {
      chatRef.current.scrollTop = chatRef.current.scrollHeight;
    }
  }, [chat]);

  return (
    <div className="App container-fluid" style={{ backgroundColor: '#ffe6e6' }}> {/* 배경색 변경 */}
      <div className="row">
        <div className="col-3 bg-light" style={{ minHeight: '100vh' }}>
          <h3 className="text-center my-3">Sidebar</h3>
          {/* Sidebar content goes here */}
        </div>
        <div className="col-9">
          <header className="App-header bg-primary text-white py-3">
            <div className="d-flex align-items-center">
              <img src={chatbotImage} alt="Chatbot" style={{ height: '40px', marginRight: '15px' }} />
              <h3>My Chatbot</h3>
            </div>
          </header>
          <div
            className="chat-window bg-white rounded"
            ref={chatRef}
            style={{
              height: '60vh',
              overflow: 'auto',
              padding: '20px',
              border: '1px solid #e0e0e0',
              marginBottom: '20px',
            }}
          >
            {chat.map((msg, index) => (
              <div key={index} className="mb-2 p-2 rounded bg-light text-dark shadow-sm">
                {msg}
              </div>
            ))}
          </div>
          <div className="chat-input input-group">
            <input
              type="text"
              className="form-control"
              value={message}
              onChange={e => setMessage(e.target.value)}
            />
            <button className="btn btn-primary" onClick={handleSend}>
              Send
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
