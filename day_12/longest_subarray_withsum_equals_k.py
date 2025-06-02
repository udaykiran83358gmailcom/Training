# longest sub array with sum equals k
n=[1,2,3,4,5,1,1,1,1]
# n=[2,0,0,3]
st=0
sumi=n[0]
max_len=0
k=3
# better
# d={}

# for i in range(len(n)): 
#     sumi+=n[i]
#     if sumi==k:
#         max_len=i+1
#     if sumi-k in d :
#         max_len=max(max_len,i-d[sumi-k])
#     if sumi not in d:
#         d[sumi]=i
# print(max_len)
# optimal
for i in range(1,len(n)):
    while sumi>=k:
        
        if sumi==k:
            max_len=max(max_len,i-st+1)
        sumi-=n[st]


        st+=1
    sumi+=n[i]
print(max_len)




