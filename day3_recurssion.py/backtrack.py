# def sub(n,a,b):
#     if n>1:
#         sub(n=n-a,a,b)
def sub(n,a,b):
    if n==1:
        return True
    if n<1:
        return False
    return sub(n-a,a,b) or sub(n-b,a,b)
    


n=int(input())
a,b=3,5
print(sub(n,a,b))
