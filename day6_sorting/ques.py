a=[7,2,6,3,6,7,7,2,2,2]
counti = {}
for x in a:
    counti[x] = counti.get(x, 0) + 1
# print(b)
# print(counti)
# for i in range(len(a)-1):
#     f=False
#     for j in range(len(a)-1-i):
#         if counti[a[j]]>counti[a[j+1]]:
#                 a[j],a[j+1]=a[j+1],a[j]
#                 f=True
#     if f==False:
#             break
k=list(counti.values())
for i in range(len(k)-1) :
    for j in range((len(k)-1)):
        if k[j]>k[j+1]:
            k[j],k[j+1]=k[j+1],k[j]
counti={v:k for k,v in counti.items()}
k=[]
for i,j in counti.items():
    k.append(i*str(j))
print(" ".join(reversed(k)))