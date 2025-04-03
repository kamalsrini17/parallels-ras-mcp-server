# Parallels RAS MCP Server (Python)

This MCP server provides a REST API backend to interact with Parallels Remote Application Server (RAS) for session management.

## Features
- List current sessions via the RAS REST API
- Simple client library for integrating with the MCP server
- FastAPI-based backend

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ras-mcp-server.git
cd ras-mcp-server
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
sessions = client.get_sessions()
print(sessions)
```


## License
MIT License
