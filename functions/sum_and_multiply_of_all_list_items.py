def sum(list):
    sum=0
    for x in list:
        sum=sum+x
    return sum
items=list((10,20,30,40,50))
print(sum(items))


def multiply(numbers):
    multiple=1
    for num in numbers:
        multiple=multiple*num
        
    return multiple
print(multiply(items))