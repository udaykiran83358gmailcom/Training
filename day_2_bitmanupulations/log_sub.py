n=[1,2,3,2,3,4,5,6,7,8,9]
k=1
maxi=0
p=[1,]
for i in range(1,len(n)):
    if n[i]-n[i-1]==1:
        k+=1
    else:
        p.append(k)
        k=1
p.append(k)
print(max(p))

