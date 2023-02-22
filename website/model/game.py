# import category

class Game:
    idGame:int
    name: str
    releaseDate: str
    synopsis: str
    video: str
    classification: int
    keyWord: str
    image: object

    def __init__(self, idGame, name, releaseDate, synopsis, video, 
                 classification, keyWord,image):
        self.idGame = idGame
        self.name = name
        self.releaseDate = releaseDate
        self.synopsis = synopsis
        self.video = video
        self.classification = classification
        self.keyWord = keyWord
        self.image = image

    def setCategory(self, nameCategory):
        self.nameCategory = nameCategory

    def json(self):
        return({
            'idGame': self.idGame,
            'name': self.name,
            'releaseDate':self.releaseDate,
            'synopsis': self.synopsis,
            'video':self.video,
            'classification':self.classification,
            'keyWord':self.keyWord,
            'imageBg':self.image.imageBg,
            'imageCard':self.image.imageCard
        })