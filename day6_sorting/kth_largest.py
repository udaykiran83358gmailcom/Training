n=list(map(int,input().split()))
k=int(input())
t=[]
p=-1
for _ in range(len(n)-1):
    for i in range(0,len(n)-1):
        if n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]
    if n[p] not in t:
        t.append(n[p])
    p=p-1
    # print(p)
t.append(n[p])
print(n)
print(t[k-1])
