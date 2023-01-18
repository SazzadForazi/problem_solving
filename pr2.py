def revarseList(arr,s,e):
    while(s<e):
        arr[s],arr[e]=arr[e],arr[s]
        s+=1
        e-=1

arr=[1,2,3,4,5,6,7,8,9]
n= len(arr)
print(arr)
revarseList(arr,0,n-1)
print(arr)
