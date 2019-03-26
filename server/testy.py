import requests
import pickle

r = requests.get("http://0.0.0.0:8080/encodings")

data = pickle.loads(r.content)
print(data["names"])

