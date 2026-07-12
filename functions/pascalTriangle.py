def pascalTriangle(num):
    pascal=[]
    for i in range(num):
        if i == 0:
            pascal.append([1])
        else:
            newList=[1]
            lastPascalList = pascal[-1]
            for y in range(len(lastPascalList)):
                if len(lastPascalList)>y+1:
                    num = lastPascalList[y]+lastPascalList[y+1]
                    newList.append(num)
                else:
                    newList.append(1)
            pascal.append(newList)
    return pascal
            
pascalList = pascalTriangle(7)

for x in pascalList:
    for y in x:
        print(y,end="")
    print()