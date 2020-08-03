from flask_sqlalchemy import SQLAlchemy

from main import DataBase


class Message(DataBase.Model):
      _id = DataBase.Column("_id", DataBase.Integer, primary_key=True)
      username = DataBase.Column("username", DataBase.String(80), nullable=False)
      message = DataBase.Column("message", DataBase.String(100), nullable=False)

      def __init__(self, username, message):
            self.username = username
            self.message = message

def GetAllMessages():
      for msg in Message.query.all():
            msg_user = msg.username
            msg_msg = msg.message
            print(f"User: {msg_user} || Message: {msg_msg}")