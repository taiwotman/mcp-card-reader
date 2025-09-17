import requests
from app.card_reader import get_card_data

track_data = get_card_data()
payload = {
    "tool": "extract_first_name",
    "params": {"track_data": track_data}
}
response = requests.post("http://localhost:5000/mcp", json=payload)
print(response.json())
