n=[3,2,4,6,5,7,1,3]
res=[]
stack=[]
for i in n[::-1]:
    while stack and stack[-1]<=i:
        stack.pop()
    if not stack:
        res.append(-1)
    else:
        res.append(stack[-1])
    stack.append(i)
res.reverse()
print(res)
            