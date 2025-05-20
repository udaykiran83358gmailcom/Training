n=list(map(str,input()))
for _ in range(len(n)-1):
    for i in range(0,len(n)-1):
        if ord(n[i])>ord(n[i+1]):
            n[i],n[i+1]=n[i+1],n[i]
print("".join(n))

