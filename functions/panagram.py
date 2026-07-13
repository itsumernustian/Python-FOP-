import re
import string
alphabets = set(string.ascii_lowercase)
def panagram(words):
    lower = words.lower()
    wordSet= set(lower)
    print(wordSet)
    if wordSet >= alphabets:
        print("Panagram")
    else:
        print("Not a panagram")
        
str ="The quick brown fox jumps over the lazy dog"
panagram(str)