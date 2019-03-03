import cv2, string, random, os, requests, face_recognition
import time, pickle
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
    return r.text

def recognize():
    success = False
    data = pickle.loads(open("encodings.pickle", "rb").read())
    frame = get_photo()
    copy = frame
    save_photo(copy)

    known_face_encodings = data["encodings"]
    known_face_names = data["names"]

    face_locations = []
    face_encodings = []
    face_names = []

    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    for face_encoding in face_encodings:
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        distances = face_recognition.face_distance(known_face_encodings, face_encoding)
        print(distances, distances[0])

    if True in matches:
        success = True

    return success
