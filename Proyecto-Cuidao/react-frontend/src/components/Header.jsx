import { useNavigate } from "react-router-dom";
import '../styles/Header.css'; // Importa el archivo CSS

export default function Header() {
    const navigate = useNavigate();
    return (
        <header className="header"> {/* Aplica la clase 'header' */}
            <div className="logo-container">
                <img
                    src="/images/logoPolicia.png?height=60&width=60"
                    alt="Logo de la policia"
                    width={140}
                    height={60}
                    onClick={() => {
                        navigate("/");
                    }}
                />
            </div>
        </header>
    );
}

