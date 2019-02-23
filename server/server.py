import flask
import requests
import cv2 
import pickle
import face_recognition

app = flask.Flask(__name__)

@app.route("/recognize", methods=["POST"])
def racognize():
    
    data = {"success": False}

    if flask.request.method == "POST":
        if flask.request.files.get("image"):

            image = flask.request.files.get('image')
            image.save("img.jpg")

            encodings = pickle.loads(open("encodings.pickle", "rb").read())
            known_face_encodings = encodings["encodings"]
            known_face_names = encodings["names"]
            frame = face_recognition.load_image_file("img.jpg")

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
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
                    face_names.append(name)

                    data["success"] = True
                    data["name"] = face_names[0]
                    data["distance"] = min(distances)
                    print(data)


                    
                
            return flask.jsonify(data)
       

            
@app.route("/user", methods=["POST", "GET"])
def create_user():
    if flask.request.method == "POST":
        user_name = flask.request.form.get('username')
        print(user_name)
        r = requests.post("http://127.0.0.1:8008/action")
        return "Dodano użytkownika pomyślnie"

    if flask.request.method == "GET":
        return flask.render_template('user.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8080')