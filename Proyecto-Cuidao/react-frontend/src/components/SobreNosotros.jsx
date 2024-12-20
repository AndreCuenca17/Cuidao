import React, { useState } from 'react';

const styles = {
  container: {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '40px 20px',
    fontFamily: '"Segoe UI", Tahoma, Geneva, Verdana, sans-serif',
    color: '#333',
    lineHeight: 1.6,
    
  },
  header: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    marginBottom: '40px',
  },
  title: {
    fontSize: '2.5em',
    fontWeight: 'bold',
    color: '#0f4c35',
    marginBottom: '20px',
    textAlign: 'center',
  },
  imageContainer: {
    width: '100%',
    height: '200px',
    backgroundColor: '#f0f0f0',
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: '30px',
    border: '1px dashed #ccc',
    borderRadius: '8px',
  },
  imagePlaceholder: {
    color: '#999',
    fontSize: '1.2em',
  },
  section: {
    marginBottom: '30px',
    borderBottom: '1px solid #e0e0e0',
    paddingBottom: '30px',
  },
  sectionHeader: {
    display: 'flex',
    alignItems: 'center',
    gap: '15px',
    cursor: 'pointer',
    padding: '15px 0',
    transition: 'background-color 0.3s',
  },
  sectionHeaderHover: {
    backgroundColor: '#f9f9f9',
  },
  toggleIcon: {
    width: '30px',
    height: '30px',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    border: '2px solid #0f4c35',
    borderRadius: '50%',
    fontSize: '20px',
    color: '#0f4c35',
    transition: 'all 0.3s',
  },
  sectionTitle: {
    fontSize: '1.5em',
    fontWeight: 'bold',
    color: '#0f4c35',
  },
  content: {
    padding: '20px 0 20px 45px',
    animation: 'fadeIn 0.5s ease-out',
  },
  bulletPoint: {
    margin: '15px 0',
    paddingLeft: '25px',
    position: 'relative',
  },
  bullet: {
    position: 'absolute',
    left: '0',
    color: '#0f4c35',
    fontSize: '1.2em',
  },
  justification: {
    backgroundColor: '#f5f5f5',
    padding: '20px',
    borderRadius: '8px',
    marginTop: '20px',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)',
  },
  justificationTitle: {
    fontSize: '1.2em',
    fontWeight: 'bold',
    marginBottom: '10px',
    color: '#0f4c35',
  },
  teamMember: {
    display: 'flex',
    alignItems: 'center',
    gap: '15px',
    margin: '20px 0',
  },
  avatar: {
    width: '50px',
    height: '50px',
    borderRadius: '50%',
    backgroundColor: '#0f4c35',
    color: 'white',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    fontSize: '20px',
    fontWeight: 'bold',
  },
  memberName: {
    fontSize: '1.1em',
    fontWeight: 'bold',
  },
  button: {
    backgroundColor: '#0f4c35',
    color: 'white',
    padding: '10px 20px',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    fontSize: '1em',
    fontWeight: 'bold',
    marginTop: '20px',
    transition: 'background-color 0.3s',
  },
  buttonHover: {
    backgroundColor: '#0f4c35',
  },
  '@keyframes fadeIn': {
    from: { opacity: 0, transform: 'translateY(-10px)' },
    to: { opacity: 1, transform: 'translateY(0)' },
  },
};

export default function AboutUs() {
  const [expandedSections, setExpandedSections] = useState({
    idea: false,
    foundations: false,
    team: false,
  });
  const [hoveredSection, setHoveredSection] = useState(null);
  const [isButtonHovered, setIsButtonHovered] = useState(false);

  const toggleSection = (section) => {
    setExpandedSections(prev => ({
      ...prev,
      [section]: !prev[section]
    }));
  };

  return (
    <div style={styles.container}>
      <div style={styles.header}>
        <h1 style={styles.title}>ABOUT US</h1>
        
      </div>

      <div style={styles.section}>
        <div 
          style={{
            ...styles.sectionHeader,
            ...(hoveredSection === 'idea' ? styles.sectionHeaderHover : {})
          }}
          onClick={() => toggleSection('idea')}
          onMouseEnter={() => setHoveredSection('idea')}
          onMouseLeave={() => setHoveredSection(null)}
        >
          <div style={{
            ...styles.toggleIcon,
            transform: expandedSections.idea ? 'rotate(45deg)' : 'none'
          }}>
            {expandedSections.idea ? '×' : '+'}
          </div>
          <h2 style={styles.sectionTitle}>Nuestra idea</h2>
        </div>
        {expandedSections.idea && (
          <div style={styles.content}>
            <p>Somos un equipo de estudiantes apasionados por la tecnología y las matemáticas, trabajando en un innovador proyecto para el curso de Matemática Discreta.</p>
            <div style={styles.bulletPoint}>
              <span style={styles.bullet}>•</span>
              Explorar una plataforma colaborativa diseñada para mapear zonas peligrosas en Lima utilizando datos recopilados por los propios usuarios.
            </div>
            <div style={styles.bulletPoint}>
              <span style={styles.bullet}>•</span>
              Registrar robos e incidentes delictivos en tiempo real.
            </div>
            <div style={styles.bulletPoint}>
              <span style={styles.bullet}>•</span>
              Visualizar en un mapa interactivo las áreas con mayores índices de criminalidad.
            </div>
            <div style={styles.justification}>
              <h3 style={styles.justificationTitle}>Justificación</h3>
              <p>
                En las últimas fechas, la delincuencia en Lima ha aumentado de manera alarmante, afectando la calidad de vida de sus habitantes. Existe una necesidad urgente de abordar este problema que se ha convertido en un tema constante de inseguridad. Esto resalta la necesidad de herramientas innovadoras que ayuden a mitigar los riesgos, informando a los ciudadanos sobre zonas de alto peligro y permitiéndoles tomar decisiones más seguras en su día a día.
              </p>
            </div>
          </div>
        )}
      </div>

      <div style={styles.section}>
        <div 
          style={{
            ...styles.sectionHeader,
            ...(hoveredSection === 'foundations' ? styles.sectionHeaderHover : {})
          }}
          onClick={() => toggleSection('foundations')}
          onMouseEnter={() => setHoveredSection('foundations')}
          onMouseLeave={() => setHoveredSection(null)}
        >
          <div style={{
            ...styles.toggleIcon,
            transform: expandedSections.foundations ? 'rotate(45deg)' : 'none'
          }}>
            {expandedSections.foundations ? '×' : '+'}
          </div>
          <h2 style={styles.sectionTitle}>Fundamentos matemáticos y algorítmicos del proyecto</h2>
        </div>
        {expandedSections.foundations && (
          <div style={styles.content}>
            <div style={styles.bulletPoint}>
              <span style={styles.bullet}>•</span>
              Teoría de Grafos para modelar redes de crimen y optimizar rutas de patrullaje
            </div>
            <div style={styles.bulletPoint}>
              <span style={styles.bullet}>•</span>
              Lógica Proposicional para sistema de clasificación de delitos
            </div>
            <div style={styles.bulletPoint}>
              <span style={styles.bullet}>•</span>
              Teoría de Conjuntos para análisis de zonas de riesgo
            </div>
            <div style={styles.bulletPoint}>
              <span style={styles.bullet}>•</span>
              Probabilidad y Estadística para predicción de tendencias delictivas
            </div>
          </div>
        )}
      </div>

      <div style={styles.section}>
        <div 
          style={{
            ...styles.sectionHeader,
            ...(hoveredSection === 'team' ? styles.sectionHeaderHover : {})
          }}
          onClick={() => toggleSection('team')}
          onMouseEnter={() => setHoveredSection('team')}
          onMouseLeave={() => setHoveredSection(null)}
        >
          <div style={{
            ...styles.toggleIcon,
            transform: expandedSections.team ? 'rotate(45deg)' : 'none'
          }}>
            {expandedSections.team ? '×' : '+'}
          </div>
          <h2 style={styles.sectionTitle}>Nuestro Equipo</h2>
        </div>
        {expandedSections.team && (
          <div style={styles.content}>
            <div style={styles.teamMember}>
              <div style={styles.avatar}>A</div>
              <span style={styles.memberName}>Cuenca Echevarría, Andre</span>
            </div>
            <div style={styles.teamMember}>
              <div style={styles.avatar}>C</div>
              <span style={styles.memberName}>Giron Altamirano, Miguel</span>
            </div>
            <div style={styles.teamMember}>
              <div style={styles.avatar}>E</div>
              <span style={styles.memberName}>Suyco Rivera, Jesus </span>
            </div>
            
          </div>
        )}
      </div>
    </div>
  );
}