n=[2,13,4,2,9,9,5,8,7,13,3]
k=3
t=max(n)+1
arr=[0]*(t)
for i in n:
    arr[i]=arr[i]+1
print(arr)
while k!=0:
    while arr[t-1]!=0 and k!=0:
        arr[t-1]-=1
        k-=1
    t-=1
    

print(t)