import flask

app = flask.Flask(__name__)

@app.route('/user', methods=["POST"])
def send_photo():
    url = flask.request.remote_addr
    print(url)# get number of photos
    return 0

app.run(port=8008)