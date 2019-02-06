from imutils.video import VideoStream
import face_recognition
import pickle
import imutils
import time
import cv2


def save_photo(p):
    title = input("Photo name: ")
    cv2.imwrite("{}.png".format(title), p)

print("[LOG] Running ...")

bartek_image = face_recognition.load_image_file("bartek1.png")
bartek_image2 = face_recognition.load_image_file("bartek2.jpg")
bartek_encoding = face_recognition.face_encodings(bartek_image)[0]
bartek_encoding2 = face_recognition.face_encodings(bartek_image2)[0]

known_face_encodings = [
    bartek_encoding,
    bartek_encoding2,
]

known_face_names = [
    "bartek",
    "bartek",
]

face_locations = []
face_encodings = []
face_names = []

vs = VideoStream(src=0).start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0) # wait for heat camera 

input("Press Enter")

frame = vs.read()

face_locations = face_recognition.face_locations(frame)
face_encodings = face_recognition.face_encodings(frame, face_locations)

face_names = []

for face_encoding in face_encodings:
    print("Petla")
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    print(matches)
    print(face_recognition.face_distance(known_face_encodings, face_encoding))

    name = "Unknown"

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]

    face_names.append(name)

if bool(face_names) == True:
    print("Na zdjęciu znajduje się: {}".format(face_names[0]))
else:
    print("Nie znaleziono")

vs.stop()