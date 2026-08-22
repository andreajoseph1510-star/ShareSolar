import pandas as pd
from fastapi import FastAPI
from backend import voice  # import your voice.py router

app = FastAPI()

# --- Root route ---
@app.get("/")
def root():
    return {"message": "ShareSolar backend is running"}

# --- Household Data ---
@app.get("/households")
def households():
    try:
        df = pd.read_csv("backend/data/solar_data.csv")
        return df.to_dict(orient="records")
    except Exception as e:
        return {"error": f"Failed to load households: {e}"}

# --- Community Summary ---
@app.get("/summary")
def get_summary():
    try:
        df = pd.read_csv("backend/data/solar_data.csv")
        total_generation = int(df["generation"].sum())
        total_usage = int(df["usage"].sum())
        total_excess = int(df["excess"].sum())
        return {
            "total_generation": total_generation,
            "total_usage": total_usage,
            "total_excess": total_excess
        }
    except Exception as e:
        return {"error": f"Failed to load summary: {e}"}

# --- Voice Features ---
app.include_router(voice.router)
