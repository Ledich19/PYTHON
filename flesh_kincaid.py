import re

file_name = input('Enter file: ')
if len(file_name) < 1:
    file_name = 'three_men_in_a_boat.txt'
file = open(file_name, 'r')
text = file.read()

counts = dict()
syllables_count = 0
amount_words = len(text.split())
amount_sentences = len(re.split(r'[.!?]', text)) - 1

words_collection = text.split()


def count_syllables(word):
    vowels = "aeiouy"
    count = 0
    word = word.lower()
    if word[0] in vowels:
        count += 1
    for flesh_kincaid_index in range(1, len(word)):
        if word[flesh_kincaid_index] in vowels and word[flesh_kincaid_index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count


syllables_count = sum(count_syllables(word) for word in words_collection)

average_length_of_words_in_sentences = amount_words / amount_sentences
average_syllables = syllables_count / amount_words
flesh_kincaid_index = 0.39 * average_length_of_words_in_sentences + \
    11.8 * average_syllables - 15.59
flesh_kincaid_index = round(flesh_kincaid_index)

print(amount_words, average_syllables)
print('Grade: ', flesh_kincaid_index)

if flesh_kincaid_index > 90:
    print('Text understandable for college or university students.')
elif flesh_kincaid_index < 60:
    print('Text understandable for 7th-8th grade students.')
else:
    print('Very complex text that may be difficult to understand even for specialists in the field.')
