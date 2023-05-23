import json
words = open('words.txt','r')
print(words)
data = []

for line in words:
  new_arr = line.split('\t\t')
  obj = {
    "word": {
      "ru": new_arr[2].strip(),
      "en": new_arr[0].strip()
    },
    "transcription": {
      "en": new_arr[1].strip()
    },
    "examples": [],
  }
  data.append(obj)

with open("words.json", "w") as file:
  json.dump(data, file , ensure_ascii=False, indent=2)
