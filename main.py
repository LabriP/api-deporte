import pandas as pd
from fastapi import FastAPI

app = FastAPI()

df = pd.read_csv("resumen_equipos.csv")

@app.get("/equipos/resumen")
def resumen():
    return df.to_dict(orient="records")
