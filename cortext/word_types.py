class WordType:
    pass

class Noun(WordType):
    def __init__(self, word, image_url=None):
        self.word = word
        self.image_url = image_url

class Organization(WordType):
    def __init__(self, word, abstract='', logo_url=None):
        self.word = word
        self.abstract = abstract
        self.logo_url = logo_url

class Celebrity(WordType):
    def __init__(self, word, abstract='', image_url=None):
        self.word = word
        self.abstract = abstract
        self.image_url = image_url

class Musician(WordType):
    def __init__(self, word, abstract='', playlist_url=None, image_url=None):
        self.word = word
        self.abstract = abstract
        self.playlist_url = playlist_url
        self.image_url

class Actor(WordType):
    def __init__(self, word, abstract='', image_url=None, imdb_url=None):
        self.word = word
        self.abstract = abstract
        self.image_url = image_url
        self.imdb_url = imdb_url

class Event(WordType):
    def __init__(self, word, abstract='', time=None):
        self.word = word
        self.abstract = abstract
        self.time = time

class Location(WordType):
    def __init__(self, word, abstract='', map_url=None):
        self.word = word
        self.abstract = abstract
        self.map_url = map_url

class Verb(WordType):
    def __init__(self, word, image_url=None):
        self.word = word
        self.image_url = image_url

class Adjective(WordType):
    def __init__(self, word, image_url=None):
        self.word = word
        self.image_url = image_url

class Color(WordType):
    def __init__(self, word):
        self.word = word
        
class Link(WordType):
    def __init__(self, word):
        self.word = word
        
class Unknown(WordType):
    def __init__(self, word):
        self.word = word
        





# -ORGANIZATION,
# -CELEBRITY,
# -MUSICIAN,
# -ACTOR,
# HUMAN,
# -MOTION_VERB, COGNITION_VERB,
# -EVENT,
# -LINK,
# LOCATION,
# -COLOR,
# -ADJECTIVE,
# -NOUN,
# -UNKNOWN = range(5)
