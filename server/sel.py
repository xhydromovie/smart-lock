import wget, os

url = 'http://0.0.0.0:8080/image'
path = os.getcwd()

wget.download(url, path)