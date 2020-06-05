import json
data = json.load(open("data.json"))

def translate(w):
  w = w.lower()
  if w in data:
    return data[w]
  elif w.title() in data:
    return data[w.title()]
  elif w.upper() in data:
    return data[w.upper()]
  elif len(get_close_matches(w,data.keys())) > 0:
    yes_no = input("Did you mean %s instead? Enter Yes/No" % get_close_matches(w,data.keys())[0])
    if yes_no.lower() in ["y","yes"]:
      return data[get_close_matches(w,data.keys())[0]]
    elif yes_no.lower() in ["n","no"]:
      return "The word doesn't exist.Please cross-check the spelling."
    else:
      return "We did not understand your chioce. It should either be yes or no"
  else:
    return "The word doesn't exist.Please cross-check the spelling."

word = input("Enter the word: ")
output = translate(word)

if type(output) == list:        # if output is list
  for item in output:
    print(item)
else:
  print(output)                  # if output is string
