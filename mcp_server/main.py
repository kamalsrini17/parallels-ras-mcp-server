from fastapi import FastAPI, HTTPException
from .ras_client import RASClient
import requests

app = FastAPI()
ras_client = RASClient()

@app.get("/sessions")
def list_sessions():
    try:
        return ras_client.get_sessions()
    except requests.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@app.post("/publish")
def publish_application(app_name: str, target_path: str, start_in: str = None, parameters: str = None):
    try:
        return ras_client.publish_application(app_name, target_path, start_in, parameters)
    except requests.HTTPError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
