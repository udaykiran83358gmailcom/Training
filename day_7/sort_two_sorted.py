n=[2,4,5,8,9]
k=[3,5,6,9,11,12,13]
s=[]
l,m=0,0
while (l<len(n)-1 and m<len(k)-1):
    if n[l]>k[m]:
        s.append(k[m])
        m+=1
    else:
        s.append(n[l])
        l+=1
if l==len(n)-1:
    s.extend(k[m:])
if m==len(k)-1:
    s.extend(n[l:])
print(s)

