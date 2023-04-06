from collections import defaultdict

n = int(input())
k = int(input())

graph = defaultdict(list)

for _ in range(k):
    row = list(map(int, input().split()))
    if row[0] == 1:
        graph[row[1]].append(row[2])
        graph[row[2]].append(row[1])

    else:
        if not graph[row[1]]:
            continue
  
        print(*graph[row[1]])
