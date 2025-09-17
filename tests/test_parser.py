from app.mcp_server import extract_first_name

def test_valid_track():
    data = "%B1234567890123456^DOE/JOHN^2405..."
    assert extract_first_name(data) == "JOHN"

def test_invalid_track():
    data = "InvalidData"
    assert extract_first_name(data) == "Invalid data"
