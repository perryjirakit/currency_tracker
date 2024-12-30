import requests
import os
from dotenv import load_dotenv
from plyer import notification

load_dotenv()

api_key = os.getenv("api_key")

url = "https://api.fxratesapi.com/latest?api_key={api_key}&base=USD&currencies&resolution=1h&amount=1&places=6&format=json"

response = requests.request("GET", url) 

# print(response.text) # use this line to see available currency.
try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    data = response.json()
    usd_to_thb = data['rates']['THB']
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    print(f'Other error occurred: {err}')

def push_notification(rate):
    # Display the notification
    notification.notify(
        title="Currency Tracker",
        message=f"Current USD to THB rate: {rate}",
        timeout=15  # Notification stays for 15 seconds
    )

push_notification(usd_to_thb)