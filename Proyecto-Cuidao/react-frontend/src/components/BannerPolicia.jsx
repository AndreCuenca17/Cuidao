import { useState, useEffect } from 'react';
import '../styles/BannerPolicial.css';

export default function Header() {
  const [currentDate, setCurrentDate] = useState('');

  useEffect(() => {
    const date = new Date();
    const options = { 
      year: 'numeric', 
      month: 'long', 
      day: '2-digit'
    };
    setCurrentDate(date.toLocaleDateString('es-ES', options));
  }, []);

  return (
    <header className="header-container">
      <div className="banner">
        <img 
          src="/images/banner.png?height=60&width=60" 
          alt="Servicios Policiales Banner" 
          className="banner-image"
        />
        <div className="banner-text">
         
        </div>
      </div>
      <nav className="nav-bar">
        <div className="date">{currentDate}</div>
        <div className="contact-info">
          <span>📞 Línea de Consulta y Atención: 980122403</span>
        </div>
        <div className="social-links">
          <a href="#" aria-label="Facebook"><i className="fab fa-facebook"></i></a>
          <a href="#" aria-label="Twitter"><i className="fab fa-twitter"></i></a>
          <a href="#" aria-label="Google Plus"><i className="fab fa-google-plus"></i></a>
          <a href="#" aria-label="LinkedIn"><i className="fab fa-linkedin"></i></a>
          <select className="country-select" defaultValue="Peru">
            <option value="Peru">Perú</option>
            {/* Add more countries as needed */}
          </select>
        </div>
      </nav>
    </header>
  );
}

