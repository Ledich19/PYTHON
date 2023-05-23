import re

file_name = input('Enter file: ')
if len(file_name) < 1:
    file_name = 'test.txt'
file = open(file_name, 'r', encoding="utf-8")
text = file.read()

counts = dict()
number_of_difficult_words = 0
amount_letters = len(''.join(filter(str.isalpha, text)))
amount_words = len(text.split())
amount_sentences = len(re.split(r'[.!?]', text)) - 1

words_collection = text.split()

def count_syllables(word):
    vowels = "aeiouy"
    count = 0
    word = word.lower()
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count


for word in words_collection:
    amount_syllables = count_syllables(word)
    if amount_syllables > 2:
        number_of_difficult_words += 1

average_length_of_words_in_sentences = amount_words / amount_sentences
percentage_difficult_words = (number_of_difficult_words / amount_words) * 100
gunning_fog_index = 0.4 * average_length_of_words_in_sentences + \
    percentage_difficult_words
gunning_fog_index = round(gunning_fog_index)

print(amount_words, number_of_difficult_words)
print('Grade: ', gunning_fog_index)

if gunning_fog_index < 9:
    print('Easy-to-understand text, suitable for a wide audience.')
elif gunning_fog_index < 13:
    print('Moderately complex text, suitable for educated readers.')
elif gunning_fog_index < 17:
    print('Complex text, requiring a higher level of education.')
else:
    print('Very complex text that may be difficult to understand even for specialists in the field.')
