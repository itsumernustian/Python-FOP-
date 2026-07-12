import re
def panagram(words):
    matched=re.findall(r'[A-Za-z]',words)
    if matched:
        print("Panagram")
    else:
        print("Not a panagram")
        
panagram("The  lazy do")