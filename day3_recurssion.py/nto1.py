# def back(n,i):
#     if i<0:
#         return
#     back(n,i-1)
#     print(i)
# n=5
# back(n,n)
def back (n,i):
    if i>n:
        return
    back(n,i+1)
    print(i)
n=3
back(n,0)
