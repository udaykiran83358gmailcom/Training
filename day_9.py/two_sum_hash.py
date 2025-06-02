n=[1,2,3,4,5,9]
tar=14
hash={}
for i,j in enumerate(n):
    if tar-j in hash:
        print(i,hash[tar-j])
        break
    else:
        hash[j]=i
else:
    print(-1)