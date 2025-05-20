n=[1,1,1,2,2]
dic={}
for i in n:
    dic[i]=dic.get(i,0)+1
m=0
res=0
for i,j in dic.items():
    if j>m:
        res=i
        m=j
print(res)

 