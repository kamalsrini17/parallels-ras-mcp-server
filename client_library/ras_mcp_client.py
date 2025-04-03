import requests

class RASMCPClient:
    def __init__(self, mcp_url):
        self.mcp_url = mcp_url

    def get_sessions(self):
        response = requests.get(f"{self.mcp_url}/sessions")
        response.raise_for_status()
        return response.json()

    def publish_application(self, app_name, target_path, start_in=None, parameters=None):
        payload = {
            "app_name": app_name,
            "target_path": target_path,
            "start_in": start_in,
            "parameters": parameters
        }
        response = requests.post(f"{self.mcp_url}/publish", json=payload)
        response.raise_for_status()
        return response.json()
