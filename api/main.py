from fastapi import FastAPI, Request
import requests

app = FastAPI()

@app.get("/api/proxy")
async def proxy(url: str):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
