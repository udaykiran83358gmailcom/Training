n=[2,3,5,6,7,7,8,9,10,10,13,15]
t=4
f=0
l,k=0,len(n)-1
while k>=l:
    mid=(l+k)//2
    if n[mid]==t:
        print(mid)
        f=1
        break
    elif n[mid]>t:
        l=0
        k=mid+1
    else:
        l=mid+1
print((l+k)/2)
 