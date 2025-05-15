n=[2,2,1,1,4,4,5,6,6]
for i in range(0,len(n)-1,2):
    if n[i]!=n[i+1]:
        print(n[i])
        break
else:
    print(n[-1])


    
