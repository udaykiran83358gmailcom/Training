def rev(a,i,k):
    if i==len(a):
        return
    rev(a,i+1,k)
    k.append(a[i])




a=[1,2,3,4]
k=[]
print(rev(a,0,k))
print(k)
