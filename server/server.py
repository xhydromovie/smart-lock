from time import gmtime, strftime
import flask
import requests
import os

app = flask.Flask(__name__)
            
@app.route("/user", methods=["POST", "GET"])
def create_user():
    if flask.request.method == "POST":
        user_name = flask.request.form.get('username')
        print(flask.request.args.get("success"))
        cwd = os.getcwd()
        path_known = cwd + "/static/photos/users"
        path_unknown = cwd + "/static/photos/unknown"

        user_path = path_known + "/" + user_name

        if not os.path.exists(user_path):
            os.mkdir(user_path)
            print("Directory created!")
        else:
            print("Directory already exists!")
            return "This user already exists!"

        print(user_name)
        return "Successfuly created!"

    if flask.request.method == "GET":
        return flask.render_template('user.html')

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
            path_known = cwd + "/photos/users"
            path_unknown = cwd + "/photos/unknown"

            if success == "true":
                try:
                    image.save(path_known + "/" + username + '/' + date + ".jpg")
                except:
                    image.save(path_unknown + ".jpg")
        else:
            return "Nie ma zdjecia"
        
        return "Blad"

    if flask.request.method == "GET":
        return flask.render_template('entry.html')

@app.route("/encodings", methods=["GET"])
def image():
    if flask.request.method == "GET":
        return flask.send_file("encodings.pickle", as_attachment=True, attachment_filename="encodings.pickle")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)