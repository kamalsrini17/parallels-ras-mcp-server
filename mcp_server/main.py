from fastapi import FastAPI
from .ras_client import RASClient

app = FastAPI()
ras_client = RASClient()

@app.get("/sessions")
def list_sessions():
    return ras_client.get_sessions()
