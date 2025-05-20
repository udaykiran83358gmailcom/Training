n=[2,13,4,2,9,9,5,8,7,13,3]
k=3
t=max(n)+1
arr=[0]*(max(n)+1)
for i in n:
    arr[i]=arr[i]+1
print(arr)
while(k!=0):
    if arr[t-1]!=0:
        k-=1
    t-=1
print(t)


