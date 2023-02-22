from website import app
from flask import make_response, jsonify, request
from website.services import gameServices
from flask_cors import cross_origin

@app.route('/games/images', methods=['GET'])
@cross_origin()
def getAllGames():
    response = gameServices.getAllGamesServices()
    return make_response(
        jsonify(response)
    )
