n=list(map(int,input().split()))
for _ in range(len(n)-1):
    f=False
    for i in range(len(n)-i-1):
        if n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]
            f=True
    if f==False:
        break
print(n)


