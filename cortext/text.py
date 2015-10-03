import nltk


class Text:

    def __init__(self, raw_text):
        self.raw_text = raw_text

    def parse(self):
        sentences = nltk.sent_tokenize(self.raw_text)
        tokens = [nltk.word_tokenize(sentence) for sentence in sentences]
        return [nltk.pos_tag(words) for words in tokens]
