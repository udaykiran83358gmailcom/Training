n="vignesh"
from collections import Counter
k=Counter(n)
print(k)
k['g']=10
k['f']=8
print(k)
# dic={v:k for k,v in k.items()}
# dic=dict()
# for i in n:
#     dic[i]=dic.get(i,0)+1
# for i,j in dic.items():
#     print(i,j)
# for i,j in k.items():
#     k[j]=i
k={v:k for k,v in k.items()}

print(k)
# x=[1,2,3,4]
# for i in x:
#     i=10
# print(x)
# for i in range(4):
#     x[i]=10
# print(x)
