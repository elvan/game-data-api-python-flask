from db import db


class GameModel(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    team_1 = db.Column(db.String(100), nullable=False)
    team_2 = db.Column(db.String(100), nullable=False)
    stadium = db.Column(db.String(100), nullable=False)
