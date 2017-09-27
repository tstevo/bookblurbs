import markovify

with open("/home/tom/Documents/Python/BookBlurbs/scraper/romance-authors.txt") as f:
    authortext = f.read()
with open("/home/tom/Documents/Python/BookBlurbs/scraper/romance-blurbs.txt") as f:
    blurbtext = f.read()

text_model1 = markovify.NewlineText(authortext)
text_model2 = markovify.Text(blurbtext)

for i in range(5):
    with open('/home/tom/Documents/Python/BookBlurbs/generator/generated.txt', 'a') as f:
    	#f.write(text_model1.make_sentence(tries=100))
    	#f.write('\n')
        f.write(text_model2.make_sentence(tries=400))
        f.write('\n')