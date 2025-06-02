n=[2,3,1,1,4]
# n=[2,1,4,5,1,2,4,2,1,1,2]
le=len(n)-1
l=1
maxi=n[0]
t=1
while l<=le-1:
    if maxi>=le:
        print(t)
        break
    max=0
    for j in range(l,maxi+1):
        if n[j]>max:
            max=n[j]
    l=maxi
    maxi+=max
    t+=1


    

    





        





