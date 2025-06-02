s="()([]{})"
stack=[]
for i in s:
    if i=='(' or i=='[' or i=='{':
        stack.append(i)
    elif not stack:
        print(False)
        break
    else:
        ch=stack[-1]
        if (ch=='(' and i==')') or (ch=='{' and i=='}') or (ch=='[' and i==']'):
            stack.pop()
        else:
            print(False)
            break
if stack:
    print(False)
else:
    print(True)
        
