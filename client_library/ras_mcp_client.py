import requests

class RASMCPClient:
    def __init__(self, mcp_url):
        self.mcp_url = mcp_url

    def get_sessions(self):
        return requests.get(f"{self.mcp_url}/sessions").json()
