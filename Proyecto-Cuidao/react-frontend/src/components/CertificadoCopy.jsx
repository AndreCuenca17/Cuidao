import { Link } from 'react-router-dom';
import Header from './BannerPolicia';
import '../styles/CertificadoCopy.css';

export default function CertifiedCopy() {
  return (
    <div className="certified-copy-page">
      <Header bannerImage="/path-to-your-banner-image.jpg" />
      
      <div className="certified-copy-container">
        <h2 className="certified-copy-title">
          Copia Certificada Digital de Denuncias Policiales
        </h2>
        
        <div className="buttons-container">
          <a href="https://certificados.policia.gob.pe/cerapdigital/terminos_condiciones.xhtml" className="action-button new-certificate">
              <span className="button-icon">➜</span>
              Nuevo Certificado
          </a>

          <a href="https://certificados.policia.gob.pe/cerdpdigital/validar_cerdpdigital.xhtml" className="action-button validate-certificate">
              <span className="button-icon">✓</span>
              Validar Certificado Emitido
          </a>

          <a href="https://certificados.policia.gob.pe/cerdpdigital/recuperar_cerdpdigital.xhtml" className="action-button recover-certificate">
              <span className="button-icon">↺</span>
              Recuperar Certificado
          </a>
          
        </div>

        <div className="help-options">
          <div className="option">
            <span className="option-icon">▶</span>
            <a href="https://www.policia.gob.pe/Contenido/video/Copia%20Certificada%20policial.mp4" className="option-link">
              Video Instructivo
            </a>
          </div>

          <div className="option">
            <span className="option-icon">📋</span>
            <a href="https://www.policia.gob.pe/Contenido/doc/GUIA%20RAPIDA%20PARA%20LA%20EMISION%20DE%20COPIA%20CERTIFICADA%20DIGITAL%20DE%20DENUNCIAS%20POLICIALES.pdf" className="option-link">
              Guía Copia Certificada
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

