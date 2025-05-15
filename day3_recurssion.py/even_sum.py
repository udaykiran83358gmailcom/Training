# def even(a,i,to):
#     if i==len(a):
#         return to
#     if a[i]%2==0:        
#         to+=a[i]
#     return even(a,i+1,to)
    
# def even(a,i,to):
#     if i==len(a):
#         return to
#     if a[i]%2==0:
#         to+=a[i]
#     return even(a,i+1,to)
def mul(a,i):
    if i==len(a):
        return 1
    return a[i]* mul(a,i+1)





a=[1,2,3,4]
to=0
# print(even(a,0,to))
print(mul(a,0))
