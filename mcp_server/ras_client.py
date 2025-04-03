import requests
from .config import RAS_API_URL, RAS_USERNAME, RAS_PASSWORD

class RASClient:
    def __init__(self):
        self.base_url = RAS_API_URL
        self.session = requests.Session()
        self.token = self.login()

    def login(self):
        response = self.session.post(f"{self.base_url}/auth/login", json={
            "username": RAS_USERNAME,
            "password": RAS_PASSWORD
        })
        response.raise_for_status()
        return response.json().get("access_token")

    def get_sessions(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        response = self.session.get(f"{self.base_url}/v1/sessions", headers=headers)
        response.raise_for_status()
        return response.json()

    def publish_application(self, app_name, target_path, start_in=None, parameters=None):
        headers = {"Authorization": f"Bearer {self.token}"}
        payload = {
            "name": app_name,
            "target": target_path,
            "startIn": start_in,
            "parameters": parameters
        }
        response = self.session.post(f"{self.base_url}/v1/publishing/apps", json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
