import Header from './BannerPolicia';
import '../styles/AntecedentesPoliciales.css';

export default function DigitalDesk() {
  return (
    <div className="digital-desk-page">
      <Header />
      
      <div className="digital-desk-container">
        <div className="title-container">
          <h2 className="desk-title">Trámite de Certificado de Antecedentes Policiales Digitales</h2>
          <h3 className="desk-subtitle">CERAP - DIGITAL</h3>
        </div>
        
        
        <div className="buttons-container">
          <a href="https://certificados.policia.gob.pe/cerapdigital/terminos_condiciones.xhtml" className="action-button new-certificate">
            <span className="button-icon">➜</span>
            Nuevo Trámite
          </a>

          <a href="https://certificados.policia.gob.pe/cerapdigital/validar_cerapdigital.xhtml" className="action-button validate-certificate">
            <span className="button-icon">✓</span>
            Validar Certificado Emitido
          </a>

          <a href="https://certificados.policia.gob.pe/cerapdigital/recuperar_cerapdigital.xhtml" className="action-button recover-certificate">
            <span className="button-icon">↺</span>
            Recuperar Certificado
          </a>
        </div>

        <div className="help-options">
          <div className="option">
            <span className="option-icon">▶</span>
            <a href="https://www.policia.gob.pe/Contenido/video/Cerap%20-%20Animacion.mp4" className="option-link">
              Video Instructivo
            </a>
          </div>

          <div className="option">
            <span className="option-icon">📋</span>
            <a href="https://www.policia.gob.pe/contenido/doc/MANUAL%20DE%20LA%20MESA%20DE%20PARTES%20DIGITAL%20PNP.pdf" className="option-link">
              Guías CERAP
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

