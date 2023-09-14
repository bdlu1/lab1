import requests

#print(requests.__version__)

resp = requests.get("https://raw.githubusercontent.com/bdlu1/lab1/main/lab1.py")

print(resp.text)
