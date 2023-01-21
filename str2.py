def printsubsting(string):
    list=[]
    for i in range(len(string)):
        temp = ""
        for j in range(i,len(string)):
            # print(j)
            temp+=string[j]
            # print(temp)

            list.append(temp)
    print(list)


string=input()
printsubsting(string)
