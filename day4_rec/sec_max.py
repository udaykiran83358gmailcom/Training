n=list(map(int,input().split()))
f_max,s_max=-999,-999
for i in n:
    if i>f_max:
        s_max=f_max
        f_max=i
    elif i>s_max:
        s_max=i
print(f_max,s_max)
