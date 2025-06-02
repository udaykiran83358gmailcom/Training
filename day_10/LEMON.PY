n=['5','5','5','10','20']
stack=[]

for i in n:
    t=1
    if i=='5':
        stack.append('5')
        t=0
    elif i=='10':
        if '5' in stack:
            stack.append('10')
            stack.remove('5')
            t=0
    else: 
        if stack.count('5')>=3:
            stack.remove('5')
            stack.remove('5')
            stack.remove('5')
            t=0
        elif stack.count('5')>=1 and stack.count('10')>=1:
            stack.remove('10')
            stack.remove('5')
            stack.append('20')
            t=0
        if t==1:
            print("can't sell")
            break
if t==0:
    print("can sell")




    


            



