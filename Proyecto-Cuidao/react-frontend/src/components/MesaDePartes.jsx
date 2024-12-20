import Header from './BannerPolicia';
import '../styles/MesaDePartes.css';

export default function DigitalDesk() {
  return (
    <div className="digital-desk-page">
      <Header />
      
      <div className="digital-desk-container">
        <div className="title-container">
          <h2 className="desk-title">Mesa de Partes Digital Policial</h2>
          <h3 className="desk-subtitle">MPD - PNP</h3>
        </div>
        
        
        <a href="https://mpd.policia.gob.pe/" className="new-process-button">
          <span className="button-icon">➜</span>
          Nuevo Trámite
        </a>
        

        <div className="help-options">
          <div className="option">
            <span className="option-icon">▶</span>
            <a href="https://www.policia.gob.pe/Contenido/video/VIDEO%20TUTORIAL%20PASO%20A%20PASO%202022.mp4" className="option-link">
              Ver video tutorial
            </a>
          </div>

          <div className="option">
            <span className="option-icon">📋</span>
            <a href="https://www.policia.gob.pe/contenido/doc/MANUAL%20DE%20LA%20MESA%20DE%20PARTES%20DIGITAL%20PNP.pdf" className="option-link">
              Guía Mesa de Partes Virtual
            </a>
          </div>

          <div className="option">
            <span className="option-icon">📞</span>
            <a href="tel:975019394" className="option-link">
              Línea de Consulta: 975019394
            </a>
          </div>
        </div>
      </div>
    </div>
  );
}

