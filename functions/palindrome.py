def isPalindrome(text):
    lpos=0
    rpos= len(text)-1
    while lpos <= rpos:
        if text[lpos] != text[rpos]:
            return False
        lpos=lpos+1
        rpos=rpos-1
    return True

print(isPalindrome("madem"))
txt="madam"
print(txt==txt[::-1])


list = [1,2,3,4,5,6]

print(list[::-1])