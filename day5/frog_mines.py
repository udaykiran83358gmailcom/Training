def mines(n,i,j,c,mine):
    if i==n-1 and j==n-1:
        c[0]+=1
        return
    if i==n or j==n:
        return
    if [i,j] in mine:
        return
    mines(n,i+1,j,c,mine)
    mines(n,i,j+1,c,mine)
    
n=int(input())
mine=[]
c=[0]
for i in range(n):
    mine.append(list(map(int,input().split())))
mines(n,0,0,c,mine)
print(c)