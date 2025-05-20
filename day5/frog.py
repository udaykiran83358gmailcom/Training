# def frog(i, j, n, c, blocked):
#     if i == n or j == n:
#         return

#     if (i, j) in blocked:
#         return

#     if i == n - 1 and j == n - 1:
#         c[0] += 1
#         return

    
#     frog(i + 1, j, n, c, blocked)
#     frog(i, j + 1, n, c, blocked)
def frog(i,j,n,c,b):
    if i==n or j==n:
        return
    if (i,j) in b:
        return
    if i==n-1 and j==n-1:
        c[0]+=1
        return
    frog(i+1,j,n,c,b)
    frog(i,j+1,n,c,b)

    
n = 5
blocked = {(1, 1), (3, 2), (4, 2), (2, 2)}
start_i, start_j = 1, 2
c = [0]

frog(start_i, start_j, n, c, blocked)
print("Number of valid paths:", c[0])
