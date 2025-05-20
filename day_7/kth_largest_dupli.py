
def merge_sort(arr):
    if len(arr)==1:
        return arr
    m=len(arr)//2
    l=merge_sort(arr[:m])
    r=merge_sort(arr[m:])

    return merge(l,r)
def merge(l,r):
    c=[]
    i,j=0,0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            c.append(l[i])
            i+=1
        else:
            c.append(r[j])
            j+=1
    while i<len(l):
        c.append(l[i])
        i+=1
    while j>len(r):
        c.append(r[j])
        j+=1






   
   
arr=[11,3,5,7,8,11,23]
merge_sort(arr)
print(arr)


