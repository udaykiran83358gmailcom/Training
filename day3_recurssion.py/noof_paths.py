# def sub(n,a,b):
#     if n>1:
#         sub(n=n-a,a,b)
def sub(n,a,b):
    if n==1:
        return 1
    if n<1:
        return 0
    return sub(n-a,a,b) + sub(n-b,a,b)
    


n=int(input())
a,b=3,5
print(sub(n,a,b))
