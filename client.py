import cortext.text
import cortext.visualizer
import cortext.api_keys
from subprocess import call

def v(text):
	t = cortext.text.Text(text).parse()
	visualizer = cortext.visualizer.Visualizer(t, cortext.api_keys.API_CONFIG)
	return visualizer.visualize_words()

# print([[w.__dict__ for w in s] for s in v('The chair is angry')])

a = input('~ ')
result = v(a)
for s in result:
	print()
	for w in s:
		print(w.__dict__)
		if 'image_url' in w.__dict__ and w.image_url:
			call(['display', w.image_url])

