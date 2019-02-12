import flask, face_recognition, cv2

app = flask.Flask(__name__)

@app.route("/recognize", methods=["POST"])
def racognize():
    
    data = {"success": False}

    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            image = flask.request.files["image"].read()

            
@app.route("/user", methods=["GET"])
def create_user():
    user_name = flask.request.args.get('user')
    


if __name__ == '__main__':
    app.run()