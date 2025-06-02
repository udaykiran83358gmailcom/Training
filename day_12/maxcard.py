a=[4,2,7,20,8,60,4,1]
k=3
rsum=0
lsum=sum(a[:k])
maxsum=lsum
rindex=len(a)-1
for i in range(k-1,-1,-1):
    lsum=lsum-a[i]
    rsum=rsum+a[rindex]
    maxsum=max(lsum+rsum,maxsum)
    rindex-=1
print(maxsum)