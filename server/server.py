from twilio.rest import Client
from flask_sqlalchemy import SQLAlchemy
from time import gmtime, strftime
import face_recognition
from imutils import paths
import flask
import requests
import os
import cv2
import pickle

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

def send_sms(isCorrect, user):
    if isCorrect:
        message = client.messages \
                .create(
                     body="Wlasnie " + user + " otworzyl drzwi.",
                     from_='+',
                     to='+'
                 )
    else:
        message = client.messages \
                .create(
                     body="Ktos nieznajomy probowal otworzyc drzwi!",
                     from_='+48799448810',
                     to='+48535850112'
                 )

    print("SMS - Success")

    


app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///smartlock.sqlite3'

db = SQLAlchemy(app)
class entries(db.Model):
    id = db.Column('entry_id', db.Integer, primary_key=True)
    path_to_img = db.Column(db.String(100))
    datetime = db.Column(db.DateTime)
    user = db.Column(db.String(20))

    def __init__(self, path_to_img, datetime, user):
        self.datetime = datetime
        self.path_to_img = path_to_img
        self.user = user

    def __repr__(self):
        return 'Entry %r' % self.user

db.create_all()
print("Created")

@app.route("/entry", methods=["POST", "GET"])
def entry():
    if flask.request.method == "POST":
        if flask.request.files.get('image'):

            date = strftime("%Y-%m-%d_%H-%M-%S", gmtime())

            image = flask.request.files.get('image')
            username = flask.request.args.get('username')
            success = flask.request.args.get('success')
            
            print(username + " -- " + success)

            cwd = os.getcwd()
            path_known = cwd + "/static/photos/users"
            path_unknown = cwd + "/static/photos/unknown"

            if success == "true":
                send_sms(True, username)
                image.save(path_known + "/" + username + '/' + date + ".jpg")
            else:
                send_sms(False, username)
                image.save(path_unknown + "/" + date + ".jpg")
        else:
            return "Image not found"
        
        return "Blad"

    if flask.request.method == "GET":
        return flask.render_template('entry.html')

@app.route("/encodings", methods=["GET"])
def encodng():
    if flask.request.method == "GET":
        return flask.send_file("encodings.pickle", as_attachment=True, attachment_filename="encodings.pickle")

def encode():
    knownEncodings = []
    knownNames = []

    imagePaths = list(paths.list_images("static/photos/core"))
    for (i, imagePath) in enumerate(imagePaths):
        name = imagePath.split(os.path.sep)[-2]

        print(name)
        img_path = os.getcwd() + imagePath
        print(img_path)

        image = cv2.imread(imagePath)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        boxes = face_recognition.face_locations(rgb,
		    model="hog")

        encodings = face_recognition.face_encodings(rgb, boxes)

        for encoding in encodings:
            knownEncodings.append(encoding)
            knownNames.append(name)

    data = {"encodings": knownEncodings, "names": knownNames}
    f = open("encodings.pickle", "wb")
    f.write(pickle.dumps(data))
    f.close()

@app.route("/entries", methods=["GET"])
def entries():
    if flask.request.method == "GET":

        return flask.render_template("entries.html")


@app.route("/user", methods=["POST"])
def users():
    if flask.request.method == "POST":
        if flask.request.files.get('image'):
            image = flask.request.files.get('image')
            username = flask.request.args.get('username')
            print(username)
            cwd = os.getcwd()
            path = cwd + "/static/photos/core/" + username + "/"
            img_path = path + username + ".jpg"

            path_db = cwd + "/static/photos/users/" + username + "/"
 
            if not os.path.isdir(path):
                os.mkdir(path)
                image.save(img_path)
            else:
                return "User exists!"

            if not os.path.isdir(path_db):
                os.mkdir(path_db)
            else:
                return "User exists!"
            
            encode()

            return "test"

        else:
            return "No photo"

@app.route("/", methods=["GET"])
def home():
    return "HOMEPAGE"

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, host="0.0.0.0", port=8080)
