import math
def bini(n,curr):
    if len(curr)==3:
        print(curr)
        return
    bini(n,curr+'0')
    bini(n,curr+'1')

a=int(input())
n=int(math.log(a,2))+1
bini(n,"")

