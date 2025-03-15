import requests
import json

ride = {
    "PULocationID": 10,
    "DOLocationID": 50, 
    "trip_distance": 40
}

url = 'http://127.0.0.1:9696/predict'
url = 'http://0.0.0.0:9696/predict'
response = requests.post(url, json = json.dumps(ride))
print(response.json())


