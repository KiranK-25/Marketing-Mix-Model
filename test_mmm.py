import requests
import json

url = "http://127.0.0.1:5000/predict"

# Put your actual feature names and values here
payload = {
    "TV_Spend": 120000,
    "Digital_Spend": 45000,
    "Social_Media_Spend": 25000,
    "Email_Spend": 8000,
    "Radio_Spend": 15000
}

response = requests.post(url, json=payload)
print(response.json())