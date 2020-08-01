from flask import Flask, render_template

main = Flask(__name__)

@main.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    main.run(port="8000")