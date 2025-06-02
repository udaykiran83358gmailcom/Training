n=[1,2,4,5,4]
i,j=0,len(n)-1
if n[i]==n[i+1]:
    print(n[i])
if n[j]==n[j-1]:
    print(n[j])
while i<j:
    if n[i]==n[j]:
        print(n[i])
        break
    else:
        j-=1
