from collections import defaultdict

n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)


graph = defaultdict(list)

for i in range(n):
    for j in range(n):

        if mat[i][j]:
           graph[i + 1].append(j + 1)
 
for key, val in graph.items():
    print(str(len(val)), *val)

