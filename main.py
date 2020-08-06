from flask import Flask
from flask import render_template
from flask import request, Response
from flask import redirect, url_for

from flask_sqlalchemy import SQLAlchemy
import bcrypt

from MessageDataBase import *


""" MAIN CONFIG """

main = Flask(__name__)

main.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Message.sqlite3"
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DataBase = SQLAlchemy(main)

text_encoder = 'utf-8'


""" WEBSITE ROUTES """

@main.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        message = request.form["message"]

        query = Message(str(username), str(message))

        DataBase.session.add(query)
        DataBase.session.commit()

        WriteToJson()

        return render_template("index.html")
    else:
        WriteToJson()

        return render_template("index.html")

@main.route("/signup", methods=["POST", "GET"])
def SingUp():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashedPassword = bcrypt.hashpw(bytes(password, text_encoder), bcrypt.gensalt())

        print(f"Password: {password}")
        print(f"Hash: {hashedPassword}")

        return redirect(url_for("index"))
    else:
        return render_template("signup.html")



@main.route("/del")
def delete():
    DeleteAll()
    WriteToJson()
    return redirect(url_for("index"))

""" Start """

if __name__ == "__main__":
    DataBase.create_all()
    main.run(port="8000")