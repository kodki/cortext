class Visualizer:

    def __init__(self, text):
        self.text = text

    def visualize_words(self):
        '''classify words for visualization
           download info from apis based on classes
           return a dict {word_id: word_info}
        '''
        classified = [self.classify_word(word)
                      for word
                      in text.tagged_tokens]
        return classified

    def classify_word(self, word):
        # search in wordnet based on tag
        return word_classes.ORGANIZATION
