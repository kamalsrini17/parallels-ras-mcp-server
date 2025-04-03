# Parallels RAS MCP Server (Python)

This MCP server provides a REST API backend to interact with Parallels Remote Application Server (RAS) for session management and app publishing.

## Features
- List current sessions via the RAS REST API
- Publish remote applications
- Simple client library for integrating with the MCP server
- FastAPI-based backend

## Setup

1. Clone the repository:
```bash
git clone https://github.com/kamalsrini17/parallels-ras-mcp-server.git
cd parallels-ras-mcp-server
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set environment variables in `.env`:
```env
RAS_API_URL=https://your-ras-server/ras/api
RAS_USERNAME=your-username
RAS_PASSWORD=your-password
```

4. Run the server:
```bash
bash run.sh
```

## Client Usage
```python
from client_library.ras_mcp_client import RASMCPClient

client = RASMCPClient("http://localhost:8000")
print(client.get_sessions())

response = client.publish_application(
    app_name="Notepad",
    target_path="C:\\Windows\\System32\\notepad.exe"
)
print(response)
```

## Submit to MCP
Submit your MCP server at [https://mcp.so/submit](https://mcp.so/submit)

## License
MIT License
