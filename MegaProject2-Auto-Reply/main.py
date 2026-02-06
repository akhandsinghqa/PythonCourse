import time

from ai_client import gemini_ai
from select_copy_data import copy_data, paste_data

while True:
    copied_data = copy_data()
    gemini_response = gemini_ai(copied_data)
    paste_data(gemini_response)
    time.sleep(30)
