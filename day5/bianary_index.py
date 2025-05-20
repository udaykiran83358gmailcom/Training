k=int(input())
t=[]
s=list(map(int,input().split()))
for i in range(k):
    t.append(list(map(int,input().split())))
row,col=len(t),len(t[0])
s=s[len(s)-1:-1:-1]
f=[]
for i in t:
    z=[]
    for j in range(len(i)-1,-1,-1):
        z.append(i[j]*(s[j]**j))
    f.append(sum(z))
# print(f)
for i,j in zip(t,f):
    print(i,j)  