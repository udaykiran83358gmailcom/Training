def island(arr,i,j,n):
    if i<0 or j<0 or i==n or j==n or arr[i][j]==0 or arr[i][j]==2:
        return
    if arr[i][j]==1:
        arr[i][j]=2
    island(arr,i+1,j,n)
    island(arr,i-1,j,n)
    island(arr,i,j+1,n)
    island(arr,i,j-1,n)
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
c=0
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            island(arr,i,j,n)
            c+=1
print(c)


    
    