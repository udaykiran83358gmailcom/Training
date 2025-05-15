def check(d,i):
    if i==len(d):
        return
    x=(prime(d[i],2,0))
    if x==0:
        print("prime")
    else:
        print("not prime")
    check(d,i+1)
def prime(p,i,c):
    if i>(p**0.5):
        return c
    if p%i==0:
        c+=1
    return prime(p,i+1,c)

d=[2,3,4]
check(d,0)
# def check(d, i):
#     if i == len(d):
#         return
#     if d[i] <= 1:
#         print("not prime")
#     else:
#         x = prime(d[i], 2, 0)
#         if x == 0:
#             print("prime")
#         else:
#             print("not prime")
#     check(d, i + 1)

# def prime(p, i, c):
#     if i > (p ** 0.5):
#         return c
#     if p % i == 0:
#         c += 1
#     return prime(p, i + 1, c)

# # Test
# d = [1, 2, 3, 4]
# check(d, 0)
