import cv2, string, random, os, requests
import time
from imutils.video import VideoStream


def get_photo():
    vs = VideoStream().start()
    time.sleep(1)
    frame = vs.read()
    vs.stop()
    return frame

def save_photo(photo):
    path = os.getcwd()+"/temp/{}.jpg".format(generate_id())
    cv2.imwrite(path, photo)
    return path

def generate_id(length=6, chars=string.ascii_uppercase):
    return "".join(random.choice(chars) for _ in range(length))

def delete_photo(path):
    os.remove(path)
    print("Photo at path: {} deleted...".format(path))

def send_photo(path, url):
    files = {'image': open(path, 'rb')} 
    r = requests.post(url, files=files)
    delete_photo(path)
    print(r.text)

send_photo(save_photo(get_photo()), 'http://127.0.0.1:5000/recognize')