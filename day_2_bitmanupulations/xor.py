n,m=5,10
def find(p):
    if p%4==1:
        ans=1
    elif p%4==2:
        ans=p+1
    elif p%4==3:
        ans=0
    else:
        ans=p
    return ans
y=find(n-1)
x=find(m)
print(x^y)