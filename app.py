import json

data = json.load(open("data.json"))

def search(w):
    if w in data:
        return data[w]
    else:
        return "The word doesn't exists! Please double check it!"

word = input("Enter a word:")

print(search(word))
