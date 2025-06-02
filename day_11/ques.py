n=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=5
maxi=sum(n[:k])
curr=maxi
for i in range(k,len(n)):
    curr=curr-n[i-k]+n[i]
    maxi=max(curr,maxi)
print(maxi)

