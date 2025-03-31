import json
import requests


x = requests.get(url="http://localhost:8090/cosmos")
a = json.loads(x.text)
print(a["message"])

