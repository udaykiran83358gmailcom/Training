n=[0,3,8,1,5,7,9]
m=[5,7,10,2,6,9,11]
l,r=0,0
dic={}
for i in range (len(m)):
    dic[m[i]]=i
m.sort()
# print(m)
c=1
k=m[0]
while l<=len(m)-1:
    if dic[m[l]]>k: 
        c+=1
        k=m[l]
        l+=1
    else:
        l+=1
print(c)
