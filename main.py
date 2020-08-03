from flask import Flask, render_template, request

# from flask_sqlalchemy import SQLAlchemy

""" MAIN CONFIG """

main = Flask(__name__)

# main.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///DataBase.sqlite3"
# main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# DataBase = SQLAlchemy(main)

""" GLOBAL VARIABLES """

Msgs = ["Hello World"]

""" WEBSITE ROUTES """

@main.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":

        username = request.form["username"]
        message = request.form["message"]

        GetAllMessages()

        print(Msgs)

        return render_template("index.html", messages=Msgs)

    else:
        print(Msgs)

        GetAllMessages()
        return render_template("index.html", messages=Msgs)



""" Start """

if __name__ == "__main__":
    DataBase.create_all()
    main.run(port="8000")