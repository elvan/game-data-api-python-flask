from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from db import db
from models import GameModel
from schemas import GameSchema

blp = Blueprint("Games", "games", description="Operations on games")


@blp.route("/game/<string:game_id>")
class Game(MethodView):
    @blp.response(200, GameSchema)
    def get(self, game_id):
        game = GameModel.query.get_or_404(game_id)
        return game

    def delete(self, game_id):
        game = GameModel.query.get_or_404(game_id)
        db.session.delete(game)
        db.session.commit()
        return {"message": "Game deleted"}, 200


@blp.route("/game")
class GameList(MethodView):
    @blp.response(200, GameSchema(many=True))
    def get(self):
        return GameModel.query.all()

    @blp.arguments(GameSchema)
    @blp.response(201, GameSchema)
    def post(self, game_data):
        game = GameModel(**game_data)
        try:
            db.session.add(game)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A game with that date already exists.",
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the game.")

        return game
