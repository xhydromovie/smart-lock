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

vs = VideoStream().start()
# vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0) # wait for heat camera 

while True:
    k = input("Press 'p' for photo, press 'q' for exit: ")

    if k == 'p':
        photo = vs.read()
        save_photo(photo)
    elif k == 'q':
        break
        
print("Stopping camera and exit...")
vs.stop()