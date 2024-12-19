import React, { useEffect, useState } from 'react';
import Home from './Home'; // Importamos el componente Home

const UbicacionPage = () => {
  const [ubicacion, setUbicacion] = useState(null);
  const [mostrarHome, setMostrarHome] = useState(true); // Mostrar Home al inicio
  const [cargando, setCargando] = useState(true); // Estado para controlar el mensaje de carga

  // Función para obtener la ubicación del usuario automáticamente al cargar la página
  const obtenerUbicacion = () => {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition((position) => {
        const lat = position.coords.latitude;
        const lon = position.coords.longitude;

        // Enviar la ubicación al backend
        fetch('http://localhost:5000/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            latitud: lat,
            longitud: lon
          })
        })
          .then(response => response.json())
          .then(data => {
            console.log("Ubicación recibida desde el backend:", data);
            setUbicacion(data); // Guardamos la respuesta de la ubicación

            // Después de guardar las coordenadas, generar los mapas
            return generarMapas();
          })
          .then(() => {
            setCargando(false); // Cambiamos el estado a false una vez que todo se ha ejecutado
          })
          .catch(error => {
            console.error('Error al procesar las funciones:', error);
            setCargando(false); // Si hay un error, también cambiamos a false para evitar que quede en carga
          });
      }, (error) => {
        console.error("Error obteniendo la ubicación:", error);
        setCargando(false); // Si hay un error en la geolocalización, cambiamos a false
      });
    } else {
      alert("La geolocalización no está disponible en tu navegador.");
      setCargando(false); // Si no hay soporte para geolocalización, también cambiamos a false
    }
  };

  // Función para generar los mapas (después de obtener la ubicación)
  const generarMapas = () => {
    return fetch('http://localhost:5000/', {
      method: 'GET', // Solicitar la generación de los mapas
    })
      .then(response => response.json())
      .then(data => {
        console.log("Mapas generados correctamente", data);
      })
      .catch(error => console.error('Error al generar los mapas:', error));
  };

  // Usamos useEffect para ejecutar obtenerUbicacion solo una vez después de que Home se haya renderizado
  useEffect(() => {
    if (mostrarHome) {
      setTimeout(() => {
        obtenerUbicacion(); // Ejecutar las funciones después de un pequeño retraso
      }, 500); // Pequeño retraso de medio segundo para asegurar que Home se muestre primero
    }
  }, [mostrarHome]); // Esto se ejecuta solo cuando `mostrarHome` cambia

  // Mientras tanto, mostramos el componente Home
  return (
    <div>
      {mostrarHome ? (
        <Home />
      ) : (
        <div>
          <h1>Ubicación Actual</h1>
          {cargando ? (
            <p>Cargando ubicación y generando mapas...</p>
          ) : (
            <div>
              {ubicacion ? (
                <div>
                  <p>Latitud: {ubicacion.latitud}</p>
                  <p>Longitud: {ubicacion.longitud}</p>
                </div>
              ) : (
                <p>No se pudo obtener la ubicación.</p>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
};

export default UbicacionPage;
