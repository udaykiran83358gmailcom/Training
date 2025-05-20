n=list(map(int,input().split()))
k=2
for i in range(k,len(n)-k):
    for j in range(len(n)-k):
        if n[i]>n[j]:
            n[i],n[j]=n[j],n[i]
print(n)