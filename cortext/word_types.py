class WordType:
    pass

class Organization(WordType):
    def __init__(self, abstract='', logo_url=None):
        self.abstract = abstract
        self.logo_url = logo_url

class Celebrity(WordType):
    def __init__(self, abstract='', image_url=None):
        self.abstract = abstract
        self.image_url = image_url

class Musician(WordType):
    def __init__(self, abstract='', playlist_url=None, image_url=None):
        self.abstract = abstract
        self.playlist_url = playlist_url
        self.image_url
        

ORGANIZATION,
CELEBRITY,
MUSICIAN,
ACTOR,
HUMAN,
MOTION_VERB,
EVENT,
LINK,
LOCATION,
COGNITION_VERB,
COLOR,
ADJECTIVE,
NOUN,
UNKNOWN = range(5)

#POLITICIAN,
#MUSICIAN,
#ACTOR,

