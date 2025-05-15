def rev(n,re):
    if n==0:
        return re
    b=n%10
  
    return rev(n//10,re*10+b)
def sumo(k,i):
    if i==k:
        return 0
    return i+sumo(k,i+1)
n=153
print(rev(n,0))
print(sumo(5,0))


