import React, { useState } from "react";
import Header from "./components/Header";
import Sidebar from "./components/Sidebar";
import MapViewer from "./components/MapViewer";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'; // Usa Routes en lugar de Switch
import UbicacionPage from './components/Ubicacion'; // Importa el componente Ubicacion
import CrimeForm from './components/CrimeForm';
import SobreNosotros from "./components/SobreNosotros";
import Home from "./components/Home";
import DigitalComplaint from "./components/DenunciaDigital";
import CertifiedCopy from "./components/CertificadoCopy";
import MesaPartes from "./components/MesaDePartes";
import CitasLinea from "./components/CitasLinea";
import AntecedentesPoliciales from "./components/AntecedentesPoliciales";
import './styles/App.css';
import FloatingChatBot from './components/FloatingChat';

const App = () => {
    const [mapUrl, setMapUrl] = useState("http://localhost:5000/map");

    const handleOptionChange = (option, checked) => {
        const params = new URLSearchParams(mapUrl.split('?')[1] || '');
        params.set(option, checked.toString());
        setMapUrl(`http://localhost:5000/map?${params.toString()}`);
    };

    return (
        <Router>
            <div className="App">
                <Header />
                <div style={{ display: "flex", flexDirection: "row", flex: 1 }}>
                    <Sidebar onOptionChange={handleOptionChange} setMapUrl={setMapUrl} />
                    <div style={{ flex: 1, overflow: 'hidden', padding: "20px" }}>
                        <Routes>
                            {/* Usa element en lugar de component */}
                            <Route path="/" element={<UbicacionPage />} />
                            <Route path="/map" element={<MapViewer mapUrl={mapUrl} />} />
                            <Route path="/efectuar-denuncia" element={<MapViewer mapUrl={mapUrl} />} />
                            <Route path="/registrar-denuncia" element={<CrimeForm mapUrl={mapUrl} />} />
                            <Route path="/sobre-nosotros" element={<SobreNosotros />} />
                            <Route path="/" element={<Home />} />
                            <Route path="/pre-registrar-denuncia" element={<DigitalComplaint />} />
                            <Route path="/CopiaCertificado" element={<CertifiedCopy />} />
                            <Route path="/mesa-partes" element={<MesaPartes />} />
                            <Route path="/citas" element={<CitasLinea />} />
                            <Route path="/antecedentesPoliciales" element={<AntecedentesPoliciales />} />
                            
                        </Routes>

                    </div>
                </div>
                <FloatingChatBot />
            </div>
        </Router>
    );
};

export default App;
