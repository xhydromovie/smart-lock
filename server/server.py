from time import gmtime, strftime
import flask
import requests
import os

app = flask.Flask(__name__)
            
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
                image.save(path_known + "/" + username + '/' + date + ".jpg")
            else:
                image.save(path_unknown + "/" + date + ".jpg")
        else:
            return "Nie ma zdjecia"
        
        return "Blad"

    if flask.request.method == "GET":
        return flask.render_template('entry.html')

@app.route("/encodings", methods=["GET"])
def encodng():
    if flask.request.method == "GET":
        return flask.send_file("encodings.pickle", as_attachment=True, attachment_filename="encodings.pickle")

@app.route("/user", methods=["POST"])
def users():
    if flask.request.method == "POST":
        if flask.request.files.get('image'):
            image = flask.request.files.get('image')
            username = flask.request.args.get('username')
            print(username)
            cwd = os.getcwd()
            path = cwd + "/static/photos/" + username

            if not os.path.isdir(path):
                os.mkdir(path)
                image.save(path + "/main.jpg")
                return "Success saved new user!"
            else:
                return "User exists!"
            
        else:
            return "No photo"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)