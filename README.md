
# Editorial Summary

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

This project bridges magnetic stripe card readers with an MCP-compliant Flask API. It extracts first names from Track 1 data and exposes them via a structured endpoint for editorial, onboarding, or demo workflows.

## Features
- Serial card reader integration
- MCP-compliant tool interface
- Modular Flask architecture
- Unit-tested parsing logic
- Ready for containerization or cloud deployment

## Usage
1. Connect your card reader via USB/Serial
2. Run `python run.py`
3. Swipe a card and POST to `/mcp` with tool `extract_first_name`

## Compliance
Ensure PCI DSS compliance when handling real cardholder data.


# 🧠 MCP Card Reader API

A modular, MCP-compliant Flask API that reads Track 1 magnetic stripe data and extracts first names for editorial, onboarding, and demo workflows. Built for reproducibility, stakeholder clarity, and secure integration.

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

No PAN or PII storage

Track 1 parsing only

Mock mode available for demos

PCI DSS-aware architecture

## 🧪 Testing

```
pytest tests/

```

## 📦 Deployment
Supports Docker and CI/CD pipelines for cloud deployment (Azure, Render, etc.)

## 🧠 Strategic Fit
Built for editorial and onboarding workflows. Supports reproducible demos, tone personalization, and scalable integration.




