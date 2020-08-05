from flask import Flask, render_template, request, url_for, Response

from MessageDataBase import *

from flask_sqlalchemy import SQLAlchemy

""" MAIN CONFIG """

main = Flask(__name__)

main.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Message.sqlite3"
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DataBase = SQLAlchemy(main)


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

@main.route("/del")
def delete():
    DeleteAll()
    return url_for(index)

""" Start """

if __name__ == "__main__":
    DataBase.create_all()
    main.run(port="8000")