def sortHyphenSeparatedString(text):
    elements = text.split("-")
    elements.sort()
    str="-".join(elements)
    print(str)
    
    # sort vs sorted()
    # join funtion 
sortHyphenSeparatedString("green-red-yellow-black-white")