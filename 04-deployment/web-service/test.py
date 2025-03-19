import requests
import json

ride = {
    "PULocationID": 10,
    "DOLocationID": 10, 
    "trip_distance": 0
}

HOST = '127.0.0.1:9696'
HOST = '0.0.0.0:9696' 
HOST = 'ride-duration-prediction-service.eba-wqx6eh2n.us-west-2.elasticbeanstalk.com' # Elastic Beanstalk Host
url = f'http://{HOST}/predict'

response = requests.post(url, json = json.dumps(ride))
print(response.json())


