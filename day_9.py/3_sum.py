n=[-1,0,-1,2,-1,-4]
s=set()
tar=0
n.sort()
for i in range(len(n)):
    j=i+1
    k=len(n)-1
    while k>j:
        z=n[i]+n[j]+n[k]
        print(z)
        print(n[i],n[j],n[k])
        if z==tar:
            s.add(((n[i]),(n[j]),(n[k])))
            j+=1
            k-=1
        elif tar>z:
            j+=1
        else:
            k-=1
    out=list(s)
    
print(out)
        
