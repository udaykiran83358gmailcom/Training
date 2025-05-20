n=input().split()
k=[]
for i in n:
    k.append([i,len(i)])
for i in range(len(k)-1):
    t=0
    for j in range(len(k)-1-i):
        if k[j][1]>k[j+1][1]:
            k[j],k[j+1]=k[j+1],k[j]
            t=1
    if t==0:
        break
for i,j in k:
    print(i,end=" ")

