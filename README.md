#cortext

a library for annotating text with images 

#usage

```python
import cortext


raw text:str -> cortext.Text(parsed natural language) 
url = "http://www.bbc.com/news/uk-34432386"

article = cortext.load_from_url(url)

# article is cortext.Text {original, parsed, relationship}

visualizer = cortext.Visualizer(article)
visualizer.visualize_words() # 
visualizer.visualize_sentences() # 
visualizer.visualize_keywords()
visualizer.visualize_persons()
visualizer.visualize_locations()
visualizer.visualize_timeline()
visualizer.original_images()
visualizer.visualize_word(word)
visualizer.visualize_sentence(sentence)
visualizer.visualize()

# visualizer.visualize_<x>() returns mapping
# of words/sentences and image sets
# or lists or image sets
# visualize calls a standard set of visualize_<x> methods
# and returns a mapping of the results
# a mapping is just a `dict` for now
# we want to easily convert to json for prototype
# it maps a word/sentence id with the image set

# hover links: open in cortext extension

```




