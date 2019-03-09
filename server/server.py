from time import gmtime, strftime
import flask
import requests
import os

app = flask.Flask(__name__)
            
@app.route("/user", methods=["POST", "GET"])
def create_user():
    if flask.request.method == "POST":
        user_name = flask.request.form.get('username')
        cwd = os.getcwd()
        path_known = cwd + "/photos/users"
        path_unknown = cwd + "/photos/unknown"

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
        if flask.request.files.get("image"):
            date = strftime("%Y-%m-%d_%H-%M-%S", gmtime())
            image = flask.request.files.get('image')

            image.save(date + ".jpg")

            

# @app.rout('/encode', methods=["POST"])
#     if flask.request

if __name__ == '__main__':
    app.run(debug=True)