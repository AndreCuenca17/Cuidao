import Header from './BannerPolicia';
import '../styles/CitasLinea.css';

export default function DigitalDesk() {
  return (
    <div className="digital-desk-page">
      <Header bannerImage="/path-to-your-banner-image.jpg" />
      
      <div className="digital-desk-container">
        <div className="title-container">
          <h2 className="desk-title">Reserva de Citas en Línea - Trámite de Lunas Oscurecidas</h2>
          
        </div>
        
        <a href="https://sistemas.policia.gob.pe/LunasCitas/cita.aspx" className="action-button">
            <span className="button-icon">➜</span>
            Nueva Cita
        </a>

      </div>
    </div>
  );
}