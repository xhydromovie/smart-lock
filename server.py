from flask import Flask, request
app = Flask(__name__)

@app.route("/attempts", methods = ['POST', "GET"])
def attempts():
    if request.method == "POST":
        print("Otworzono drzwi")
    else:
        request.method == "GET"
        print("Historia otworzen")
    
    return "Ok"

if __name__ == '__main__':
    app.run()