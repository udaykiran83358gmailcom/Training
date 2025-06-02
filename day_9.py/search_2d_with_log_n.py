n=n=[[2,4,6,30],[5,7,9,40],[8,12,13,50],[20,23,26,60],[30,35,40,70]]
key=23
def bin(n,key):
    l,r=0,len(n)-1
    while l<=r:
        mid=(l+r)//2
        if n[mid]==key:
            return mid
        elif n[mid]>key:
            r=mid-1
        else:
            l=mid+1
k=len(n[0])-1
s=[]
for i in range(len(n)):
    s.append(n[i][k])
for i in n:
    j=n.index(i)
    i.pop()
    i.extend(s)
    t=bin(i,key)
    if t!=None:
        print(j,t)
    
   

