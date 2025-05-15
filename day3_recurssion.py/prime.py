
def prime(n,i,c):
    if i>(n**0.5):
        return c
    if n%i==0:
        c+=1
    return prime(n,i+1,c)

    
n=30
x=prime(n,2,0)
if x==0:
    print("prime")
else:
    print("not prime")


