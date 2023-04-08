n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)

count = 0
for i in range(n):
    for j in range(n):
        if mat[i][j]:
            count += 1

print(count // 2)
