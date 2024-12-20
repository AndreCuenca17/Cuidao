export default function MapViewer({ mapUrl }) {
    return (
        <div style={{ flex: 1, height: "calc(100vh - 88px)" }}>
            <iframe
                src={mapUrl}
                style={{
                    width: "100%",
                    height: "100%",
                    border: "none",
                }}
                title="Mapa interactivo"
            />
        </div>
    );
}
