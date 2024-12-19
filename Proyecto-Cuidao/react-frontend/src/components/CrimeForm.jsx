import React, { useState, useEffect } from 'react';

const inputStyle = {
  width: '100%',
  padding: '8px',
  marginBottom: '10px',
  border: '1px solid #ccc',
  borderRadius: '4px'
};

const labelStyle = {
  display: 'block',
  marginBottom: '5px',
  fontWeight: 'bold'
};

const buttonStyle = {
  backgroundColor: '#0077be',
  color: 'white',
  padding: '10px 20px',
  border: 'none',
  borderRadius: '5px',
  cursor: 'pointer',
  fontSize: '16px'
};

const selectStyle = {
  ...inputStyle,
  appearance: 'none',
  paddingRight: '25px',
  background: 'url("data:image/svg+xml;utf8,<svg fill=\'black\' height=\'24\' viewBox=\'0 0 24 24\' width=\'24\' xmlns=\'http://www.w3.org/2000/svg\'><path d=\'M7 10l5 5 5-5z\'/><path d=\'M0 0h24v24H0z\' fill=\'none\'/></svg>") no-repeat right 8px center',
  backgroundSize: '16px'
};

const distritosLima = [
  'Ancon', 'Ate', 'Barranco', 'Bellavista', 'Brena', 'Carabayllo', 'Carmen de La Legua-Reynoso', 'Chaclacayo', 'Callao', 'Chorrillos', 'Cieneguilla',
  'Comas', 'El Agustino', 'Independencia', 'Jesus Maria', 'La Molina', 'La Perla','La Punta', 'La Victoria', 'Cercado de Lima',
  'Lince', 'Los Olivos', 'Lurigancho', 'Lurin', 'Magdalena del Mar', 'Miraflores', 'Pachacamac',
  'Pucusana', 'Pueblo Libre', 'Puente Piedra', 'Punta Hermosa', 'Punta Negra', 'Rimac', 'San Bartolo',
  'San Borja', 'San Isidro', 'San Juan de Lurigancho', 'San Juan de Miraflores', 'San Luis',
  'San Martin de Porres', 'San Miguel', 'Santa Anita', 'Santa Maria del Mar', 'Santa Rosa',
  'Santiago de Surco', 'Surquillo', 'Ventanilla','Villa El Salvador', 'Villa Maria del Triunfo', 'Mi Peru'
];

export default function CrimeForm() {
  const [formData, setFormData] = useState({
    dni: '',
    nombres: '',
    apellidoPaterno: '',
    apellidoMaterno: '',
    celular: '',
    correo: '',
    fecha: '',
    hora: '',
    distrito: '',
    direccion: '',
    tipoDelito: '',
    otroDelito: ''
  });

  const [mapUrl, setMapUrl] = useState('http://localhost:5000/reportar-crimen'); // URL del backend que sirve el HTML del mapa
  const [errorMessage, setErrorMessage] = useState("");

  const handleMapClick = async () => {
    try {
      // Solicitar el distrito al backend
      const response = await fetch("http://localhost:5000/settear-distrito");
      if (response.ok) {
        const data = await response.json();

        // Actualizar el estado del formulario con el distrito recibido
        setFormData((prev) => ({
          ...prev,
          distrito: data.distrito,
        }));

        console.log("Distrito recibido:", data.distrito);
      } else {
        console.error("Error al obtener el distrito:", response.statusText);
      }
    } catch (error) {
      console.error("Error al realizar la solicitud:", error);
    }
  };

  useEffect(() => {
    const handleMapMessage = (event) => {
      if (event.data && event.data.type === "coordinatesSaved") {
        console.log("Coordenadas guardadas en el backend. Solicitando distrito...");
        handleMapClick(); // Llama al backend para obtener el distrito
      }
    };

    window.addEventListener("message", handleMapMessage);

    return () => {
      window.removeEventListener("message", handleMapMessage);
    };
  }, []);



  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://localhost:5000/reportar-crimen', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      if (response.ok) {
        setSuccessMessage('¡Denuncia registrada con éxito!');
        setErrorMessage(''); // Limpiar errores si la respuesta es exitosa
      } else {
        setErrorMessage('');
      }
      console.log('Respuesta del servidor:', data);
    } catch (error) {
      console.error('Error al registrar la denuncia:', error);
      setErrorMessage('');
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };



  const handleRegistrar = () => {
    // Validar si algún campo está vacío
    if (!formData.dni || !formData.nombres || !formData.apellidoPaterno || !formData.apellidoMaterno) {
      setErrorMessage("Por favor, completa todos los campos antes de registrar la denuncia.");
      return;
    }

    // Si todo está completo
    setErrorMessage(""); // Limpia el mensaje de error
    alert("¡Denuncia registrada con éxito!"); // Puedes cambiar esto por tu lógica de envío
  };

  return (
    <div style={{ maxWidth: '800px', margin: '0 auto', padding: '20px' }}>
      
      {/* Imagen encima del formulario */}
      <div style={{ marginBottom: '20px' }}>
       <img 
          src="/images/denunciaDigital.png?height=60&width=60" 
          alt="Descripción de la imagen" 
          style={{ width: '150px', height: 'auto', borderRadius: '5px' }}
        />
      </div>
      <form onSubmit={handleSubmit}>
        <div style={{ marginBottom: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '5px' }}>
          <h2 style={{ fontSize: '20px', fontWeight: 'bold', marginBottom: '15px', backgroundColor: '#f0f0f0', padding: '10px' }}>DATOS PERSONALES</h2>
          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', rowGap: '15px', columnGap: '20px', padding: '10px' }}>
            <div>
              <label style={labelStyle} htmlFor="dni">N° DNI:</label>
              <input
                style={inputStyle}
                id="dni"
                name="dni"
                value={formData.dni}
                onChange={handleInputChange}
              />
            </div>
            <div>
              <label style={labelStyle} htmlFor="nombres">Nombres:</label>
              <input
                style={inputStyle}
                id="nombres"
                name="nombres"
                value={formData.nombres}
                onChange={handleInputChange}
              />
            </div>
            <div>
              <label style={labelStyle} htmlFor="apellidoPaterno">Apellido Paterno:</label>
              <input
                style={inputStyle}
                id="apellidoPaterno"
                name="apellidoPaterno"
                value={formData.apellidoPaterno}
                onChange={handleInputChange}
              />
            </div>
            <div>
              <label style={labelStyle} htmlFor="apellidoMaterno">Apellido Materno:</label>
              <input
                style={inputStyle}
                id="apellidoMaterno"
                name="apellidoMaterno"
                value={formData.apellidoMaterno}
                onChange={handleInputChange}
              />
            </div>
          </div>
        </div>

        <div style={{ marginBottom: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '5px' }}>
          <h2 style={{ fontSize: '20px', fontWeight: 'bold', marginBottom: '15px', backgroundColor: '#f0f0f0', padding: '10px' }}>DATOS DEL CRIMEN</h2>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '20px' }}>
            <div>
              <h3 style={{ fontWeight: 'bold', marginBottom: '10px' }}>TIEMPO</h3>
              <div>
                <label style={labelStyle} htmlFor="fecha">Fecha:</label>
                <input
                  style={inputStyle}
                  type="date"
                  id="fecha"
                  name="fecha"
                  value={formData.fecha}
                  onChange={handleInputChange}
                />
              </div>
              <div>
                <label style={labelStyle} htmlFor="hora">Hora:</label>
                <input
                  style={inputStyle}
                  type="time"
                  id="hora"
                  name="hora"
                  value={formData.hora}
                  onChange={handleInputChange}
                />
              </div>
            </div>

            <div>
              <h3 style={{ fontWeight: 'bold', marginBottom: '10px' }}>UBICACIÓN</h3>
              <div>
                <label style={labelStyle} htmlFor="departamento">Departamento:</label>
                <input
                  style={inputStyle}
                  id="departamento"
                  name="departamento"
                  value="Lima"
                  readOnly
                />
              </div>
              <div>
                <label style={labelStyle} htmlFor="provincia">Provincia:</label>
                <input
                  style={inputStyle}
                  id="provincia"
                  name="provincia"
                  value="Lima Metropolitana"
                  readOnly
                />
              </div>
              <div>
                <label style={labelStyle} htmlFor="distrito">Distrito:</label>
                <select
                  style={selectStyle}
                  id="distrito"
                  name="distrito"
                  value={formData.distrito}
                  onChange={handleInputChange}
                >
                  <option value="">Seleccione un distrito</option>
                  {distritosLima.map(distrito => (
                    <option key={distrito} value={distrito}>{distrito}</option>
                  ))}
                </select>
              </div>
            </div>
          </div>

          <div style={{ marginTop: '20px' }}>
            <h3 style={{ fontWeight: 'bold', marginBottom: '10px' }}>ESPECIFICACIÓN</h3>
            <div>
              <label style={labelStyle} htmlFor="tipoDelito">Tipo de delito:</label>
              <select
                style={selectStyle}
                id="tipoDelito"
                name="tipoDelito"
                value={formData.tipoDelito}
                onChange={handleInputChange}
              >
                <option value="">Seleccione el tipo de delito</option>
                <option value="Robo">Robo</option>
                <option value="Hurto">Hurto</option>
                <option value="Otros">Otros</option>
              </select>
            </div>
            {formData.tipoDelito === 'Otros' && (
              <div style={{ marginTop: '10px' }}>
                <label style={labelStyle} htmlFor="otroDelito">Especifique el delito:</label>
                <input
                  style={inputStyle}
                  id="otroDelito"
                  name="otroDelito"
                  value={formData.otroDelito}
                  onChange={handleInputChange}
                />
              </div>
            )}
          </div>
        </div>

        {/* Área del Mapa */}
        <div style={{ marginBottom: '20px', padding: '20px', border: '1px solid #ccc', borderRadius: '5px' }}>
          <h3 style={{ fontWeight: 'bold', marginBottom: '10px' }}>Seleccione la ubicación en el mapa</h3>
          <iframe
            src={mapUrl} // Muestra el HTML del mapa servido desde el backend
            style={{
              width: '100%',
              height: '400px', // Ajusta según sea necesario
              border: 'none',
              borderRadius: '5px',
            }}
            onClick={handleMapClick} // Opcional, para manejar clics
            title="Mapa de ubicación"
          />
          <p style={{ marginTop: '10px', fontSize: '14px', color: '#666' }}>
            Haga clic en el mapa para seleccionar automáticamente el distrito
          </p>
        </div>

        {errorMessage && (
          <div style={{ display: 'flex', justifyContent: 'flex-end', marginTop: '20px', color: "red" }}>{errorMessage}</div>
        )}

        <button
          style={buttonStyle}
          onClick={handleRegistrar}
        >
          Registrar Denuncia
        </button>

      </form>
    </div>
  );
}