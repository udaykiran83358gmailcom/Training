s='abc'
l=len(s)
for i in range(0,2**l):
    sub=""
    for j in range(0,l):
        if i&(1<<j):
            sub+=s[j]
    print(sub)