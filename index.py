import json
data = json.load(open("data.json"))

def translate(w):
  if w in data:
    return data[w]
  else:
    return "The word doesn't exist.Please cross-check the spelling."

word = input("Enter the word: ")
print(translate(word))
