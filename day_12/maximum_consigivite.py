n=[1,1,1,0,0,1,1,0,0,1]
c_zero=0
k=2
l=0
max_len=0
for r in range(len(n)):
    if n[r]==0:
        c_zero+=1
    while c_zero>k:
        if n[l]==0:
            c_zero-=1
        l+=1
    
    max_len=max(max_len,r-l+1)
print(max_len)