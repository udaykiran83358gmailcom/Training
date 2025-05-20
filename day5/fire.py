def island(a, i, j, n):
    
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        return
    
    a[i][j] = 2

    
    island(a, i+1, j, n)
    island(a, i-1, j, n)
    island(a, i, j+1, n)
    island(a, i, j-1, n)

n = int(input())
k = []
c = 0

for _ in range(n):
    k.append(list(map(int, input().split())))
island(k,3-1,6-1,n)
arr=sum(k,[])
print(arr.count(1))



print("Final Grid after marking islands:")
for row in k:
    print(row)
print("Number of islands:", c)
