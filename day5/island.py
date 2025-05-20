def island(a, i, j, n):
    # Check bounds first
    print("the i ,j  and a[i][j]",i,j)
    if i < 0 or j < 0 or i >= n or j >= n or a[i][j] != 1:
        print("the i ,j  and a[i][j]",i,j)
        return
    
    # Mark the cell as visited
    a[i][j] = 2
    for row in a:
        print(row)

    # Visit all 4 directions
    print("island 1 called")
    island(a, i+1, j, n)
    print("island 2 called")
    island(a, i-1, j, n)
    print("island 3 called")
    island(a, i, j+1, n)
    print("island 4 called")
    island(a, i, j-1, n)
    

n = int(input())
k = []
c = 0

for _ in range(n):
    k.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if k[i][j] == 1:
            island(k, i, j, n)
            c += 1

print("Final Grid after marking islands:")
for row in k:
    print(row)
print("Number of islands:", c)
