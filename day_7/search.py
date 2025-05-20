n=[2,4,3,1,4,2,3,4,5]
t=10
for i in range(len(n)-1,-1,-1):
    if n[i]==t:
        print(i)
        break
else:
    print(-1)

# t=5
# l,k=0,len(n)
# while k>l:
#     mid=(l+k)//2
#     if n[mid]==t:
#         print(mid)
#         break
#     if n[mid]>t:
#         l=0
#         k=mid-1
#     else:
#         l=mid+1
#         k=k-1
