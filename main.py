import pandas as pd
from fastapi import FastAPI

app = FastAPI(title="API Análisis Deportivo")

# Cargar datos exportados desde Power BI
df = pd.read_csv("resumen_equipos.csv")

@app.get("/")
def home():
    return {"mensaje": "API funcionando correctamente"}

@app.get("/equipos/resumen")
def resumen_equipos():
    return df.to_dict(orient="records")
