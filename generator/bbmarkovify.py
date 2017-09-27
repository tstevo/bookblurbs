import markovify

# Get raw text as string.
#with open("/home/tom/Documents/Python/BookBlurbs/scraper/sherlock.txt") as f:
with open("/home/tom/Documents/Python/BookBlurbs/scraper/results.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    #print(text_model.make_sentence(tries=400))
    with open('/home/tom/Documents/Python/BookBlurbs/generator/generated.txt', 'a') as f:
                f.write(text_model.make_sentence(tries=400))
                f.write(' ')
                f.write('\n')

# Print three randomly-generated sentences of no more than 140 characters
#for i in range(3):
#    print(text_model.make_short_sentence(140))