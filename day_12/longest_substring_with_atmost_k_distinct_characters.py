s="aaabbbcccddd"
k=3
maxi=0
d={}
r=0
for i in range(len(s)):
    d[s[i]]=d.get(s[i],0)+1
    while len(d)>k:
        d[s[r]]-=1
        if d[s[r]]==0:
            del d[s[r]]
        r+=1
    maxi=max(maxi,i-r+1)
print(maxi)


