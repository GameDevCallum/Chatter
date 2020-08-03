from flask_sqlalchemy import SQLAlchemy

import numpy as np

from main import DataBase


class Message(DataBase.Model):
      _id = DataBase.Column("_id", DataBase.Integer, primary_key=True)
      username = DataBase.Column("username", DataBase.String(80), nullable=False)
      message = DataBase.Column("message", DataBase.String(100), nullable=False)

      def __init__(self, username, message):
            self.username = username
            self.message = message

def GetAllMessages():
      toReturn = []
      for msg in Message.query.all():
            msg_user = msg.username
            msg_msg = msg.message
            toReturn.append(f"Username: {msg_user} || Message: {msg_msg}")

      return np.flip(toReturn)
