def fire_wood(arr,i,j,n):
    if i<0 or j<0 or i==n or j==n or arr[i][j]==0 or arr[i][j]==2:
        return
    if arr[i][j]==1:
        arr[i][j]=2
    fire_wood(arr,i+1,j,n)
    fire_wood(arr,i-1,j,n)
    fire_wood(arr,i,j+1,n)
    fire_wood(arr,i,j-1,n)
n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))
l,k=1,1
fire_wood(arr,l,k,n)
arr=sum(arr,[])
print(arr.count(0))
