import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(w):
    if w[0].islower():
        w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn =  input("Did you mean %s instead? Enter Y for yes or N for No: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exists. Please double check it."
        else:
            return "We didn't understand your entry!"
    else:
        return "The word doesn't exists! Please double check it!"

word = input("Enter a word:")

output = search(word)

if type(output) == list:
    i= 1
    for item in output:
        print (i , ":" , item)
        i +=1
else:
    print (output)
