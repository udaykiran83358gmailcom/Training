s="abcdabcde"
k=set()
l=0
maxi=0
for i in range(len(s)):
    while  s[i] in k:
        k.remove(s[l])
        l+=1
    maxi=max(maxi,i-l+1)
    k.add(s[i])
print(maxi)
# s="abcedacefacb"
# dic={}
# l,r=0,0
# maxi=0
# m,n='c','d'
# cur=""
# while r<=len(s)-1:
#     if s[r] not in dic:
#         dic[s[r]]=r
#         r+=1
#         cur+=s[r]
#     else:
#         if dic[s[r]]>=l:
#             l=dic[s[r]]+1
#         dic[s[r]]=r
#         r+=1    
#     if m in cur and n in cur:
#         maxi=max(maxi,r-l+1)
# print(maxi)



    

