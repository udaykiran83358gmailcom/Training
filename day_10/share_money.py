arr1=[6,5,4,3,2,1][::-1]
arr2=[4,3,2,2,1,1][::-1]
l,r,t=0,0,0
while l<=len(arr2) and r<len(arr1):
    if arr2[l]>=arr1[r]:
        l+=1
        r+=1
        t+=1
    else:
        
        r+=1
print(t)

