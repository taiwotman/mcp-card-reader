
# 🧠 MCP Card Reader API

## 🧱 Project Structure
```
mcp-card-reader/
├── app/
│   ├── __init__.py
│   ├── routes.py          # Flask MCP endpoint
│   ├── mcp_server.py      # MCP tool logic
│   └── card_reader.py     # Serial card reader interface
├── client/
│   └── send_request.py    # MCP client to test endpoint
├── tests/
│   └── test_parser.py     # Unit tests for name extraction
├── config.py              # Port and baudrate settings
├── run.py                 # Entry point for Flask app
├── requirements.txt
└── README.md
```

This project bridges magnetic stripe card readers with an MCP-compliant Flask API. It extracts first names from Track 1 data and exposes them via a structured endpoint for editorial, onboarding, or demo workflows. Built for reproducibility, stakeholder clarity, and secure integration.

## ⚙️ Requirements Overview
![Flask](https://img.shields.io/badge/Flask-v2.3.3-blue.svg?longCache=true&logo=flask&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) 
![PySerial](https://img.shields.io/badge/PySerial-v3.5-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) 
![MCP--Utils](https://img.shields.io/badge/MCP--Utils-v0.1.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) 
![Requests](https://img.shields.io/badge/Requests-v2.31.0-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a) !
[Pytest](https://img.shields.io/badge/Pytest-v7.4.2-blue.svg?longCache=true&logo=python&style=flat-square&logoColor=white&colorB=5e81ac&colorA=4c566a)


## 🚀 Features
- Serial card reader integration (USB/COM)
- MCP-compliant tool interface (`extract_first_name`)
- RESTful endpoint for editorial and onboarding flows
- Unit-tested parsing logic
- Ready for containerization and CI/CD

## 🧩 Architecture
[Card Swipe] → [Serial Reader] → [Flask MCP Server] → [Track 1 Parser] → [First Name Output]


## 🛠 Usage
```bash
# Install dependencies
pip install -r requirements.txt

# Run Flask server
python run.py

# Test with client
python client/send_request.py
```

## 🔐 Compliance

- No PAN or PII storage

- Track 1 parsing only

- Mock mode available for demos

- PCI DSS-aware architecture

## 📡 MCP Request Example
```
{
  "tool": "extract_first_name",
  "params": {
    "track_data": "%B1234567890123456^DOE/JOHN^2405..."
  }
}
```

## 🧪 Testing

```
pytest tests/

```

## 📦 Deployment
Supports Docker and CI/CD pipelines for cloud deployment (Azure, Render, etc.)





