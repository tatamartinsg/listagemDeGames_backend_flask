from website.model.db.conexaodb import cursorSQL

def queryDBSelect(query):
    cursorSQL.execute(query)
    return cursorSQL.fetchall()