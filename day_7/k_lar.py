n=[3,6,4,5,3,4,2,3,6,7,8,8,7,6,7,7,1,1,1]
dic={}
k=3
for i in n:
    dic[i]=dic.get(i,0)+1
m=max(dic.values())+1
print(dic)
b=[0]*m
for i in dic:
    b[dic[i]]=i
print(b)
print(b[k-1])

