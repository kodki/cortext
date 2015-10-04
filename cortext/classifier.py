import cortext.word_types as word_types
from nltk.corpus import wordnet as wn
import urllib.request
import json


#TODO: change (word_types)
class Classifier:

    def classify_word(self, tagged_word):
        # search in wordnet based on tag
        # (yellow, 'JJ')    -> COLOR
        # (FIFA, 'NNP')     -> ORGANIZATION
        # (Placebo, 'NNP')  -> MUSICIAN
        word, tag = tagged_word
        if tag == 'JJ':
            return self.classify_adjective(word)
        elif tag.startswith('VB'):
            print(dir(self))
            return self.classify_verb(word)
        elif tag.startswith('NNP'):
            return self.classify_name(word)
        elif tag.startswith('N'):
            return self.classify_noun(word)
        else:
            return word_types.Unknown()

    def classify_adjective(self, word):
        # COLOR / ADJECTIVE
        for synset in wn.synsets(word):
            if synset.lexname() == 'noun.attribute' and 'color' in synset.definition():
                return word_types.Color()
        return word_types.Adjective()

    def classify_verb(self, word):
        # MOTION_VERB / COGNITION_VERB / UNKNOWN
        for synset in wn.synsets(word):
            if synset.lexname() in ['verb.motion', 'verb.cognition']:
                return word_types.Verb()
        return word_types.Unknown()

    def classify_noun(self, word):
        # NOUN
        return word_types.Noun()

    def classify_name(self, word):
        # ORGANIZATION / EVENT / LOCATION / <human>
        return self.fetch_dbpedia_json(word)

    def fetch_dbpedia_json(self, name):
        name = name.replace(' ', '_')
        u = "http://dbpedia.org/data/{0}.json".format(name)
        data = urllib.request.urlopen(u)
        json_data = json.loads(data.read().decode('utf8'))
        thumbnail_url = json_data[
            "http://dbpedia.org/resource/{0}".format(name)]['http://dbpedia.org/ontology/thumbnail'][0]['value']
        abstracts = [abstract['value'] for abstract in json_data[
            "http://dbpedia.org/resource/{0}".format(name)]["http://dbpedia.org/ontology/abstract"] if abstract['lang'] == 'en']
        if abstracts:
            return word_types.Celebrity(abstracts[0], thumbnail_url)
        else:
            return word_types.Unknown()

