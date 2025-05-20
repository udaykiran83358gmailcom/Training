def maze(n,i,j,c,l):
    if i==l-1 and j==l-1:
        c[0]+=1
        return
    if i==l or j==l:
        return
    if n[i][j]==0:
        return
    maze(n,i+1,j,c,l)
    maze(n,i,j+1,c,l)
n=int(input())
k=[]
c=[0]
for i in range(n):
    k.append(list(map(int,input().split())))
l=len(k[0])
maze(k,0,0,c,l)
print(c[0])
