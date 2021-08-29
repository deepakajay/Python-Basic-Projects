import json
import difflib
from difflib import get_close_matches

file=open("data.json")
data=json.load(file)


def word_translate(word):
    if word.upper() in data:
        data_list=data[word.upper()]
        for x in data_list:
            print(x)
    elif word.lower() in data:
        data_list=data[word.lower()]
        for x in data_list:
            print(x)
    elif len(get_close_matches(word,data.keys()))>0:
        value=get_close_matches(word,data.keys())[0]
        print("did you mean {} instead?".format(value))
        response=input("(Y/N)\n")
        if response=='Y' or response=='y':
            word_translate(value)
        else:
            print("word does not exist, please try again")
    else:
        print("word does not exist, please try again")

name=input("Enter the word: ")
word_translate(name.lower())
