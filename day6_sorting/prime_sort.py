def prime(x):
    for i in x:
        c=0
        for j in range(2,i//2+1):
            if i%j==0:
                c+=1
        if c==0:
            return i
n=[[4,13,12],[8,10,5],[17,10,20],[14,8,3]]
t=[]
x=[]
for i in range(len(n)):
    x.append((prime(n[i])))
for _ in range(len(n)-1):
    for j in range(len(n)-1-j):
        if x[j]>x[j+1]:
            x[j+1],x[j]=x[j],x[j+1]
            n[j],n[j+1]=n[j+1],n[j]
   
print(n)
