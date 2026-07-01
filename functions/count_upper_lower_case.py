import re
def count(text):
    upper = re.findall('[A-Z]',text)
    lower = re.findall('[a-z]',text)
    print("%s is a an uppercase letters",len(upper))
    print("%s is a an lowercase letters",len(lower))
    
    
count("The quick Brow Fox")

#  use built-in functions

def lettersCount(text):
    upper=0
    lower=0
    for x in text:
        if x.isupper():
            upper= upper+1
        else:
            if x.islower():
                lower =lower+1
    print("%s is a an uppercase letters",upper)
    print("%s is a an lowercase letters",lower)
    
lettersCount("The quick Brow Fox")

