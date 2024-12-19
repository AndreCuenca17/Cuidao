import React, { useState } from 'react';
import '../styles/Carrusel.css'; // Importa el archivo de estilo CSS

// Componente del Carrusel con imágenes y títulos predeterminados
export default function ImageCarrusel() {
    // Estado para controlar la imagen activa
    const [currentIndex, setCurrentIndex] = useState(0);

    // Lista de imágenes y títulos
    const images = [
        { url: '/images/PercepcionDelincuencia.png?height=60&width=60', title: 'Percepción de Criminalidad', des:'En Lima y Callao, 94% de ciudadanos se sienten inseguro en las calles' , link:'https://www.infobae.com/peru/2024/10/20/en-lima-y-callao-94-de-ciudadanos-se-siente-inseguro-en-las-calles/#:~:text=Lima%20se%20ha%20convertido%20en,y%20Callao%2C%20con%2090%20casos.'},
        { url: '/images/Crimen.png?height=60&width=60', title: 'Criminalidad al Alza' , des:'El 50% de la población ha afirmado haber sido víctima de la delincuencia en los últimos tres meses',link:'https://www.infobae.com/peru/2024/10/22/la-mitad-de-peruanos-afirma-que-fue-victima-de-inseguridad-en-los-ultimos-3-meses/'},
        { url: '/images/indiceSeguridad.png?height=60&width=60', title: 'Indices de Criminalidad' , des:'El informe de percepción de inseguridad ciudadana del año 2024, elaborado por el INEI, incrementó de 82.6 a 86.1 %',link:'https://rpp.pe/lima/seguridad/percepcion-de-inseguridad-ciudadana-repunta-al-861-en-primer-semestre-de-2024-segun-informe-del-inei-noticia-1579133#:~:text=Respecto%20al%20a%C3%B1o%202023%20hay,la%20cifra%20llega%20a%2088.5%20%25.'},
        { url: '/images/reporteRobo.jpg?height=60&width=60', title: 'Baja Tasa de Reporte' , des:'INEI: Solo el 15.5% de las víctimas de un hecho delictivo hacen la denuncia',link:'https://www.elperuano.pe/noticia/123704-inei-solo-el-155-de-las-victimas-de-un-hecho-delictivo-hacen-la-denuncia'},
    ];

    // Función para cambiar a la siguiente imagen
    const nextImage = () => {
        setCurrentIndex((prevIndex) => (prevIndex + 1) % images.length);
    };

    // Función para cambiar a la imagen anterior
    const prevImage = () => {
        setCurrentIndex(
            (prevIndex) => (prevIndex - 1 + images.length) % images.length
        );
    };

    return (
        <div className="carousel-container">
            <div className="carousel">
                <button className="carousel-button prev" onClick={prevImage}>
                    &#10094;
                </button>
                <div className="carousel-image-container">
                    <img
                        src={images[currentIndex].url}
                        alt={images[currentIndex].title}
                        className="carousel-image"
                    />
                    <div className="carousel-title">
                        <h2>{images[currentIndex].title}</h2>
                        <p>{images[currentIndex].des}</p>
                        <a href = {images[currentIndex].link} target= '_blank'><p>Saber mas</p></a>
                    </div>

                </div>
                <button className="carousel-button next" onClick={nextImage}>
                    &#10095;
                </button>
            </div>
        </div>
    );
}