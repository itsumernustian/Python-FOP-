# write an function that find a maximum of three numbers


def max_of_two(x,y):
    if x>y:
        return x

    return y


def max_of_three(x,y,z):
    return max_of_two(x,max_of_two(y,z))

max=max_of_three(10,6,100)
print(max)