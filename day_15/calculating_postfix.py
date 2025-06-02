n=['15','3','+','6','2','-','*']
stack=[]
for i in n:
    if i.isdigit():
        stack.append(i)
    else:
        x=int(stack.pop())
        y=int(stack.pop())
        if i=='+':
            stack.append(str(y+x))
        elif i=='-':
            stack.append(str(y-x))
        elif i=='*':
            stack.append(str(y*x))
        else:
            stack.app(str(y/x))
print(stack)
