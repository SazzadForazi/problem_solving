# str = input()
# # stringis = str.split(" ")
# # for i in range(len(stringis)):
# print(str[::-1])

def reverseStringWordWise(string):
    # print(string)
    string=string.split(" ")

    i=0
    j=len(string)-1
    while i<j:
        string[i],string[j] = string[j],string[i]
        i += 1
        j -= 1
    # print(string)
    answer =" "
    for i in string:
        answer+=i
        answer+=" "


    return answer
string = input()
ans = reverseStringWordWise(string)
print(ans)
