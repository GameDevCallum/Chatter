from flask import Flask, render_template, request

main = Flask(__name__)

@main.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

        username = request.form["username"]
        message = request.form["message"]

        print(f"User: {username} || Message: {message}"

        return render_template("index.html")
    else:
        return render_template("index.html")



if __name__ == "__main__":
    main.run(port="8000")