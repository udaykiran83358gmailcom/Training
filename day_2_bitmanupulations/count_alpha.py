from collections import Counter
n=input()
stack=[]
for i in range(len(n)):
    if len(stack)==0:
        stack.append(n[i])
    elif stack[-1]==n[i]:
        stack.append(n[i])
    else:
        print(len(stack),end="")
        print(stack[-1],end="")
        while stack:
            stack.pop()
        stack.append(n[i])

print(len(stack),end="")
print(stack[-1])
while stack:
    stack.pop()

