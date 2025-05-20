n=list(map(str,input().split()))
for _ in range(0,len(n)-1):
   for i in range(len(n)-1):
        f=False
        for k,p in zip(n[i],n[i+1]):
            t=0
            if ord(k)>ord(p) and t!=2:
                n[i],n[i+1]=n[i+1],n[i]
                f=True
                t+=1
                break
            if f==False:
                break
print(n)