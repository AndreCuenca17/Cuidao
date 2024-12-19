import { useState } from "react";
import { useNavigate } from "react-router-dom";
import "../styles/Sidebar.css";

export default function Sidebar({ onOptionChange, setMapUrl }) {
    const [showOptions, setShowOptions] = useState(false);
    const [activeButton, setActiveButton] = useState(""); // Estado para rastrear el botón activo
    const navigate = useNavigate();

    const toggleOptions = () => {
        setShowOptions((prev) => !prev);
    };

    const handleButtonClick = (path, url) => {
        setActiveButton(path); // Actualiza el botón activo
        if (url) setMapUrl(url); // Actualiza la URL si es necesario
        navigate(path); // Navega a la ruta
    };

    return (
        <div className="sidebar">
            <button
                onClick={() => {
                    toggleOptions();
                    handleButtonClick("/map", "http://localhost:5000/map");
                }}
                className={`panorama-button ${activeButton === "/map" ? "active" : ""}`}
            >
                Ver Panorama
            </button>

            {showOptions && (
                <div className="options-container">
                    {[
                        { id: "ubicacion", label: "Ubicación Actual" },
                        { id: "crimenes", label: "Mostrar Crímenes" },
                        { id: "comisarias", label: "Mostrar Comisarías" },
                        { id: "distritos", label: "Delimitar Distritos" },
                        { id: "calor", label: "Mapa de Calor" },
                    ].map((option) => (
                        <div className="option-item" key={option.id}>
                            <input
                                type="checkbox"
                                id={option.id}
                                onChange={(e) => onOptionChange(option.id, e.target.checked)}
                            />
                            <label htmlFor={option.id}>{option.label}</label>
                        </div>
                    ))}
                </div>
            )}

            <div className="navigation-buttons">
                {[
                    { path: "/efectuar-denuncia", label: "Ver Comisaria Más Cercana", url: "http://localhost:5000/efectuar-denuncia" },
                    { path: "/antecedentesPoliciales", label: "Certificado de Antecedentes Policiales" },
                    { path: "/pre-registrar-denuncia", label: "Denuncia Policial Digital" },
                    { path: "/CopiaCertificado", label: "Copia Certificada de Denuncia Policial" },
                    { path: "/mesa-partes", label: "Mesa de Partes Digital Policial" },
                    { path: "/citas", label: "Citas en Línea - Lunas Oscuras" },
                    { path: "/sobre-nosotros", label: "Sobre Nosotros" },
                    
                ].map((button) => (
                    <button
                        key={button.path}
                        className={`nav-button ${activeButton === button.path ? "active" : ""}`}
                        onClick={() => handleButtonClick(button.path, button.url)}
                    >
                        {button.label}
                    </button>
                ))}
            </div>
        </div>
    );
}