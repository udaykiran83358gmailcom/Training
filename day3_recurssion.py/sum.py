def sumi(sum,i):
    if i==0:
        print(sum)
        return
    sumi(sum+i,i-1)
sumi(0,5)
    