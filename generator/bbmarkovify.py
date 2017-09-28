import markovify

with open("/home/tom/Documents/Python/BookBlurbs/scraper/romance-titles.txt") as f:
    titletext = f.read()
with open("/home/tom/Documents/Python/BookBlurbs/scraper/romance-blurbs.txt") as f:
    blurbtext = f.read()

text_model1 = markovify.NewlineText(titletext)
text_model2 = markovify.Text(blurbtext)

for i in range(5):
    with open('/home/tom/Documents/Python/BookBlurbs/generator/generated.txt', 'a') as f:
    	f.write(text_model1.make_sentence(tries=600))
    	f.write(':')
    	f.write('\n')
        f.write(text_model2.make_sentence(tries=600))
        f.write('\n')