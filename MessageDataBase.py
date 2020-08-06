from flask_sqlalchemy import SQLAlchemy
import json

from main import DataBase

class Message(DataBase.Model):
      _id = DataBase.Column("_id", DataBase.Integer, primary_key=True)
      username = DataBase.Column("username", DataBase.String(80), nullable=False)
      message = DataBase.Column("message", DataBase.String(100), nullable=False)

      def __init__(self, username, message):
            self.username = username
            self.message = message


def WriteToJson():
      toJson = {}
      toJson['Messages'] = []
      for msg in Message.query.all():
            toJson['Messages'].append({
                  "id": msg._id,
                  "username": msg.username,
                  "message": msg.message
            })

      with open("static/MessageData.json", "w") as outfile:
            outfile.write("")
            json.dump(toJson, outfile)


def DeleteAll():
      for msg in Message.query.all():
            DataBase.session.delete(msg)
            DataBase.session.commit()