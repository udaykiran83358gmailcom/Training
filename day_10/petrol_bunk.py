n=[3,2,1,0,4]
curr=n[0]
if n[0]>=1:
    for i in range(1,len(n)):
        curr-=1
        if n[i]>curr:
            curr=n[i]
        elif curr==0:
            t=0
            break
    if t==0:
        print("not possible")
    else:
        print("possible")
else:
    print("not possible")

