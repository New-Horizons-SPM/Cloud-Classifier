import requests
from ssh import ssh

tunnel = ssh(user='ubuntu',host='118.138.241.17')   # Tunnel must be created before we can reach the nectar machine
if(not tunnel.connected):
    exit()

url = "http://127.0.0.1:8000/predict"               # Predict endpoint. 8000 comes from the default port in ssh

payload = {'scanData':  [1, 2, 3],                  # Some dummy data
           'scanSize':  (75e-9,75e-9),
           'modelName': "test_model"}

json = requests.post(url,json=payload)              # Make the post request
response = json.json()                              # Convert json to Python dictionary

prediction   = response['prediction']
errorMessage = response['error']

print('prediction', prediction)
print('error', errorMessage)
