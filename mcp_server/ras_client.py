import requests
from .config import RAS_API_URL, RAS_USERNAME, RAS_PASSWORD

class RASClient:
    def __init__(self):
        self.base_url = RAS_API_URL
        self.session = requests.Session()
        self.token = self.login()

    def login(self):
        resp = self.session.post(f"{self.base_url}/auth/login", json={
            "username": RAS_USERNAME,
            "password": RAS_PASSWORD
        })
        resp.raise_for_status()
        return resp.json().get("access_token")

    def get_sessions(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        resp = self.session.get(f"{self.base_url}/v1/sessions", headers=headers)
        resp.raise_for_status()
        return resp.json()
