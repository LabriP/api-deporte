from fastapi import FastAPI

app = FastAPI(title="API Análisis Deportivo")

@app.get("/")
def home():
    return {"message": "API funcionando"}

@app.get("/powerbi")
def powerbi_data():
    return [
        {"equipo": "Llaneros", "xG": 1.8, "tiros": 12},
        {"equipo": "Millonarios", "xG": 2.1, "tiros": 15},
        {"equipo": "Nacional", "xG": 0.9, "tiros": 8}
    ]
