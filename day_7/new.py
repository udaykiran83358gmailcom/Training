n=[3,3,3,3,2,2,4,4]
dic={}
c=1
res=n[0]
# res=0
# maxi=0
# for i in n:
#     x=dic[i]=dic.get(i,0)+1
#     if x>maxi:
#         maxi=x
#         res=i
# if maxi>len(n)//2:
#     print(res)
for i in range(1,len(n)):
    if res==n[i]:
        c+=1
    else:
        c-=1
        if c==0:
            res=n[i]
            c=1

print(res)
