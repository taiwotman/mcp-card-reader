import serial
from config import PORT, BAUDRATE, TIMEOUT

def get_card_data():
    try:
        with serial.Serial(PORT, BAUDRATE, timeout=TIMEOUT) as reader:
            return reader.readline().decode('utf-8').strip()
    except serial.SerialException as e:
        return f"Serial error: {e}"
