def perfectNumber(num):
    sum = 0
    for x in range(1,num):
        if num % x ==0:
            sum+=x
            
    return num == sum

print(perfectNumber(6))