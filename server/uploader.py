import requests

files = {'image': open('img.jpg', 'rb')}
r = requests.post('http://0.0.0.0:8080/entry', files=files)
print(r.text)