from website.model.db.query import queryDBSelect

def getAllGames():
    query = 'SELECT * FROM game NATURAL JOIN image'
    return queryDBSelect(query)