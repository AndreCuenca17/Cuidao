import { Link } from 'react-router-dom';
import Header from './BannerPolicia';
import '../styles/DenunciaDigital.css';

export default function DigitalComplaint() {
  return (
    <div className="digital-complaint-page">
      <Header bannerImage="/path-to-your-banner-image.jpg" />
      <div className="complaint-container">
        <div className="title-container">
            <h2 className="desk-title">Denuncia Policial Digital</h2>
          </div>
        
        <Link to="/registrar-denuncia" className="new-complaint-button">
          <span className="button-icon">➜</span>
          Nueva denuncia
        </Link>

        <div className="complaint-options">
          <div className="option">
            <span className="option-icon">▶</span>
            <a href="https://www.policia.gob.pe/Contenido/video/Denuncia%20Digital%20Policial%20(set%202020).mp4" className="option-link">
              Ver vídeo tutorial
            </a>
          </div>

          <div className="option">
            <span className="option-icon">📋</span>
            <a href="https://www.policia.gob.pe/Contenido/doc/GUIA%20RAPIDA%20DENUNCIA%20DIGITAL.pdf" className="option-link">
              Guía de denuncia Policial
            </a>
          </div>

          <div className="option">
            <span className="option-icon">📞</span>
            <a href="tel:980122403" className="option-link">
              Línea de Consulta: 980122403
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

