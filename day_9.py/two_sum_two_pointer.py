n=[11,1,23,14]
tar=15
s=[]
for i,j in enumerate(n):
    s.append([j,i])
s.sort()
l,r=0,len(n)-1
while r>=l:
    sum=s[l][0]+s[r][0]
    if sum==tar:
        print(l,r)
        break
    elif sum>tar:
        r-=1
    else:
        l+=1
else:
    print(-1)



