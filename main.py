from flask import Flask, render_template, request

from MessageDataBase import *

from flask_sqlalchemy import SQLAlchemy

""" MAIN CONFIG """

main = Flask(__name__)

main.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Message.sqlite3"
main.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DataBase = SQLAlchemy(main)

""" DATABASE """

# class Message(DataBase.Model):
#       _id = DataBase.Column("_id", DataBase.Integer, primary_key=True)
#       username = DataBase.Column("username", DataBase.String(80), nullable=False)
#       message = DataBase.Column("message", DataBase.String(100), nullable=False)

#       def __init__(self, username, message):
#             self.username = username
#             self.message = message


""" WEBSITE ROUTES """

@main.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        message = request.form["message"]

        query = Message(str(username), str(message))

        DataBase.session.add(query)
        DataBase.session.commit()

        
        return render_template("index.html", messages=GetAllMessages())
    else:
        GetAllMessages()
        return render_template("index.html", messages=GetAllMessages())

""" Start """

if __name__ == "__main__":
    DataBase.create_all()
    main.run(port="8000")