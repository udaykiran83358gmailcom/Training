n=[1,2,3,4,5,6,7,8,9,10]
l,r=max(n),sum(n)
while l<=r:
    days,d=5,1
    curr=0
    k=(l+r)//2
    for i in n:
        if curr+i<=k:
            curr+=i
        else:
            d+=1
            curr=i
    if d<=days:
        r=k-1
    
    else:
        l=k+1
print(l)


