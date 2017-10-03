import markovify
from bbtweeter import main

with open("/home/tom/Documents/Python/BookBlurbs/scraper/romance-titles.txt") as f:
	romtitletext = f.read()
with open("/home/tom/Documents/Python/BookBlurbs/scraper/science-titles.txt") as f:
    scititletext = f.read()
with open("/home/tom/Documents/Python/BookBlurbs/scraper/romance-blurbs.txt") as f:
	romblurbtext = f.read()
with open("/home/tom/Documents/Python/BookBlurbs/scraper/science-blurbs.txt") as f:
    sciblurbtext = f.read()

sci_model1 = markovify.NewlineText(scititletext)
sci_model2 = markovify.Text(sciblurbtext)

rom_model1 = markovify.NewlineText(romtitletext)
rom_model2 = markovify.Text(romblurbtext)

model_combo = markovify.combine([sci_model2, rom_model2],[2,1])

##write to twitter
main(model_combo.make_short_sentence(140))
print("blurb tweeted.")

##write title and combined blurb
# for i in range(3):
#     with open('/home/tom/Documents/Python/BookBlurbs/generator/generatedmix.txt', 'a') as f:
#     	# f.write(text_model1.make_sentence(tries=200))
#     	# f.write(':')
#     	# f.write('\n')
#         f.write(model_combo.make_sentence(tries=500))
#         f.write('\n')

##write scifi blurb
# for j in range(3):
# 	with open('/home/tom/Documents/Python/BookBlurbs/generator/generatedsci.txt', 'a') as f:
# 		f.write(sci_model2.make_sentence(tries=500))
# 		f.write(' ')

##add new paragraph in text file
# with open('/home/tom/Documents/Python/BookBlurbs/generator/generatedmix.txt', 'a') as f:
# 		f.write('\n\n')