s="5+6-1"
ans=""
stack=[]
def priority(x):
    if x=="^":
        return 3
    elif x=='*' or x=="/":
        return 2
    elif x=='+' or x=='-':
        return 1
    else:
        return -1
for i in s:
    if (i>='a' and i<='z') or i.isdigit()  :
        ans+=i
    elif i=='(':
        stack.append(i)
    elif i==')':
        while stack and stack[-1]!=')':
            ans+=stack[-1]
            stack.pop()
        stack.pop()
    else:
        while stack and priority(i)<=priority(stack[-1]):
            ans+=stack[-1]
            stack.pop()
        stack.append(i)
while stack:
    ans+=stack[-1]
    stack.pop()
print(ans)
k=[]
for i in ans:
    if i.isdigit():
        k.append(i)
    else:
        x=int(k.pop())
        y=int(k.pop())
        if i=='+':
            k.append(y+x)
        elif i=='-':
            k.append(y-x)
        elif i=='*':
            k.append(y*x)
        else:
            k.append(y/x)
print(*k)




