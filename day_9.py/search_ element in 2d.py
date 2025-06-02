n=[[2,4,6,30],[5,7,9,40],[8,12,13,50],[20,23,26,60],[30,35,40,70]]
key=23
# for i in range(len(n)):
#     for j in range(len(n[0])):
#         if n[i][j]==key:
#             t=0
#             print(i,j)
#             break
#     if t==0:
#         break
f=1
def binary_row(l,n,key):
    r=len(n)-1
    while l<=r:
        mid=(l+r)//2
        last=n[mid][-1]
        if last==key:
            return mid
        elif last>key:
            r=mid-1
        else:
            l=mid+1
    return l
i=0
def binary_col(l,n,key):
    r=len(n)-1
    while (l<=r):
        mid=(l+r)//2
        if n[mid]==key:
            return mid
        elif n[mid]>key:
            r=mid-1
        else:
            l=mid+1
    else:
        binary_row(i+1,n,key)
l=binary_row(0,n,key)
r=binary_col(0,n[l],key)
print(l,r)



