n=[4,3,2,1,5]
n=sorted(n)
k=[]
print(n)
sumi=sum(n)
s=0
for i in n[::-1]:
    s+=i
    k.append(sumi-s)
print(sum(k)/len(n))
