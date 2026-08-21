import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ShareSolar backend is running"}

@app.get("/households")
def households():
    df = pd.read_csv("data/solar_data.csv")
    return df.to_dict(orient="records")

@app.get("/summary")
def get_summary():
    df = pd.read_csv("data/solar_data.csv")
    total_generation = int(df["generation"].sum())
    total_usage = int(df["usage"].sum())
    total_excess = int(df["excess"].sum())
    return {
        "total_generation": total_generation,
        "total_usage": total_usage,
        "total_excess": total_excess
    }
