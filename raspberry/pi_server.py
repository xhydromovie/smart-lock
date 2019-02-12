import flask
from lib import send_photo, save_photo, get_photo

app = flask.Flask(__name__)

@app.route('/action', methods=["POST"])
def send_create():
    url = "http://" + flask.request.remote_addr + ":5000/recognize"
    send_photo(save_photo(get_photo()), url)

    return "Hello world"

app.run(debug=True, port=8008)