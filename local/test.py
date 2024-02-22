import requests
from ssh import ssh

tunnel = ssh(user='ubuntu',host='118.xxx.xxx.xx')
if(not tunnel.connected):
    exit()

url = "http://127.0.0.1:8000/predict"

payload = {'scanData':  [1, 2, 3],
           'scanSize':  (75e-9,75e-9),
           'modelName': "test_model"}

json = requests.post(url,json=payload)
response = json.json()

prediction   = response['prediction']
errorMessage = response['error']

print('prediction', prediction)
print('error', errorMessage)
