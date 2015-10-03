class Visualizer:

    def __init__(self, text):
        self.text = text
        self._classifier = classifier.Classifier()

    def visualize_words(self):
        '''classify words for visualization
           download info from apis based on classes
           return a dict {word_id: word_info}
        '''
        classified = [self._classifier.classify_word(tagged_word)
                      for tagged_word in sentence
                      for sentence
                      in text.tagged_sentences]

        return classified
