n=[2,1,6,4,2,3,1,1,4,2,6,7,3]
k=7
curr=0
st=0
maxi=0
# for i in range(len(n)):
#     curr+=n[i]
#     while curr>=k:
#         if maxi<=(i-st+1):
#             maxi=i-st+1
#         curr-=n[st]
#         st+=1
# print(maxi)f
l,r=0,0
maxi=0
while r<=len(n)-1:
    curr+=n[r]
    if curr>=k:
        if maxi<r-l+1:
            maxi=r-l+1
        curr-=n[l]
        l+=1
        r+=1

    else:
        r+=1
print(maxi)



