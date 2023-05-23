import re

file_name = input('Enter file: ')
counts = dict()

if len(file_name) < 1:
  file_name = 'three_men_in_a_boat.txt'
text = open(file_name, 'r', encoding="utf-8")
text = text.read()
text_arr = re.findall(r"\b[\w']+\b", text)

for word in text_arr:
  word = re.sub(r'[^a-zA-Zа-яА-Я\s]-', '', word.lower())
  counts[word] = counts.get(word, 0) + 1

print(len(counts))

sorted_counts = sorted(counts.items(),  key=lambda x: x[1], reverse=True)
for (word, count) in sorted_counts:
  print(word,'\u001B[34m',count,'\u001B[0m')
