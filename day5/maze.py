def check(ri,down,arr,row,col,c):
    if ri>=row or down>=col:
        return
    if arr[ri][down]==0:
        return
    if ri==row-1 and down==col-1 :
        c[0]+=1
        print(c[0])
        return
    
    check (ri+1,down,arr,row,col,c)
    check(ri,down+1,arr,row,col,c)
n=int(input())  
arr=[]
for i in range(n): 
    arr.append(list(map(int,input().split())))
c=[0]
check(0,0,arr,len(arr),len(arr[0]),c)
print(c)
