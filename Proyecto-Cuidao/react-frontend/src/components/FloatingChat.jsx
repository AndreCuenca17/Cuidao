import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import '../styles/FloatingChat.css';

const FloatingChatBot = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [prompt, setPrompt] = useState('');
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const chatContentRef = useRef(null);

  useEffect(() => {
    if (chatContentRef.current) {
      chatContentRef.current.scrollTop = chatContentRef.current.scrollHeight;
    }
  }, [messages]);

  const handleGenerate = async (e) => {
    e.preventDefault();
    if (!prompt.trim()) return;

    setIsLoading(true);
    setMessages(prev => [...prev, { text: prompt, type: 'user' }]);
    setPrompt('');

    try {
      const res = await axios.post('http://127.0.0.1:5000/generate', { prompt });
      setMessages(prev => [...prev, { text: res.data.response, type: 'bot' }]);
    } catch (error) {
      console.error('Error generating content:', error);
      setMessages(prev => [...prev, { text: 'Hubo un error al generar la respuesta.', type: 'error' }]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className={`floating-chatbot ${isOpen ? 'open' : ''}`}>
      {!isOpen && (
        <button 
          className="chat-bubble"
          onClick={() => setIsOpen(true)}
          aria-label="Abrir chat"
        >
          <svg 
            viewBox="0 0 24 24" 
            width="24" 
            height="24" 
            stroke="currentColor" 
            strokeWidth="2" 
            fill="none"
          >
            <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" />
          </svg>
        </button>
      )}
      
      {isOpen && (
        <div className="chat-window">
          <div className="chat-header">
            <h3>ChatBot: Corni</h3>
            <button 
              className="close-button"
              onClick={() => setIsOpen(false)}
              aria-label="Cerrar chat"
            >
              −
            </button>
          </div>
          
          <div className="chat-content" ref={chatContentRef}>
            {messages.map((message, index) => (
              <div 
                key={index} 
                className={`message ${message.type}`}
              >
                {message.text}
              </div>
            ))}
          </div>
          
          <form onSubmit={handleGenerate} className="chat-input">
            <input
              type="text"
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
              placeholder="Escribe tu mensaje aquí..."
              aria-label="Mensaje"
              disabled={isLoading}
            />
            <button type="submit" disabled={isLoading}>
              {isLoading ? 'Enviando...' : 'Enviar'}
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default FloatingChatBot;

