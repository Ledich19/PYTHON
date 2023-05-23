import re

file_name = input('Enter file: ')
if len(file_name) < 1 : file_name = 'test.txt'
file = open(file_name,'r')
text = file.read()

counts = dict()
amount_letters = len(''.join(filter(str.isalpha, text)))
amount_words = len(text.split())
amount_sentences = len(re.split(r'[.!?]', text)) - 1

L = amount_letters / amount_words * 100
S = amount_sentences / amount_words * 100
coleman_iau_index = 0.0588 * L - 0.296 * S - 15.8
coleman_iau_index = round(coleman_iau_index)

print(amount_letters, amount_words, amount_sentences)
print('Grade: ', coleman_iau_index)

if coleman_iau_index < 7:
  print('Easy-to-understand text, suitable for a wide audience.')
elif coleman_iau_index < 9:
  print('Moderately complex text, suitable for educated readers.')
else:
  print('Complex text, requiring a higher level of education.')
