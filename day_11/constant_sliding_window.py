# find the highset sum possible with k elements
n=[1,2,3,4,5]
k=3
l=0
r=k
maxi=sum(n[l:r])
while r<len(n):
    maxe=(maxi-n[l])+n[r]
    maxi=max(maxi,maxe)
    l+=1
    r+=1
print(maxi)