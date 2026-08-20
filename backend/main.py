import pandas as pd
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ShareSolar backend is running"}

@app.get("/households")
def households():
    import pandas as pd
    df = pd.read_csv("data/solar_data.csv")
    return df.to_dict(orient="records")
