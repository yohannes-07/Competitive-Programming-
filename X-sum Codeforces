from collections import defaultdict
n=int(input())
for i in range(n):
    n,m=list(map(int,input().split()))
    grid=[]
    for _ in range(n):
        row=list(map(int,input().split()))
        grid.append(row)

    diagonal1 = defaultdict(int)
    diagonal2 = defaultdict(int)
    for row in range(n):
        for col in range(m):
            diagonal1[row - col] += grid[row][col]
          
            diagonal2[row + col] += grid[row][col]

    max_value = 0
    for row in range(n):
        for col in range(m):
            curr_value = diagonal1[row - col] + diagonal2[row + col] - grid[row][col]
            max_value = max(max_value, curr_value)
     
    print(max_value)
