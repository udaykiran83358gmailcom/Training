def valid(n,l,r,c=""):
    if l==n and r==n:
        print(c)
        return
    if l<n:
        valid(n,l+1,r,c+'(')
    if r<l:
        valid(n,r,l+1,c+')')
n=int(input())
valid(n,0,0)