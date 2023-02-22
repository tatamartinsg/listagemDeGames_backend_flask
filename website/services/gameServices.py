from website.repositories import gameRepository
from website.model.game import Game
from website.model.image import Image


def getAllGamesServices():
    response = gameRepository.getAllGames()

    allGames = list()
    count = 0
    for game in response:
        allGames.append(
            Game(
                game[0],game[1],game[2],game[3],game[4],
                game[5],game[6], Image(game[8], game[9])
            ).json()
        )

    
    return allGames

