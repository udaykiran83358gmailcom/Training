n=[2,7,11,15]
tar=22
s=0
for i in range(len(n)):
    for j in range(i+1,len(n)):
        if n[i]+n[j]==tar:
            print(i,j)
            s=1
            break
    if s==1:
        break