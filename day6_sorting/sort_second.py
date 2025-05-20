n=int(input())
k=[]
for i in range(n):
    k.append(list(map(int,input().split())))
for _ in range(n-1):
    for i in range(n-1):
        if k[i][1]>k[i+1][1]:
            k[i][1],k[i+1][1]=k[i+1][1],k[i][1]
print(k)



        