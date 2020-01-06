import re
from googletrans import Translator
import time
TEXT = "text.txt"

f = open(TEXT, 'r')
text = f.read().split(sep=' ')
f.close()
pattern = re.compile('\w+')
translator = Translator(user_agent='Chrome/<Chrome Rev>')
words = []
for word in text:
	try:
		word = pattern.findall(word)[0].lower()
		if not word in words:
			words.append(word)
	except:
	    print('Error')
	    time.sleep(60)

words.sort()
print(words)

out_f = open('dictionary_' + TEXT, 'w')
out_f.close()

out_f = open('dictionary_' + TEXT, 'a')
out_f.write(str(len(words)) + ' unique words' + '\n')
print(str(len(words)) + ' unique words')
i = 0
for word in words:
	if i % 50 == 0:
		time.sleep(10)
	translation = translator.translate(word, dest='ru', src='en').text
	out_f.write(word + ' ' + translation + '\n')
	print(word, '-', translation)
	i += 1
out_f.close()

print('END OF PROGRAM')
