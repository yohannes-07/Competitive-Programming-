n = int(input())
mat = []
for _ in range(n):
    row = list(map(int, input().split()))
    mat.append(row)


source, sink = [], []

for i in range(n):
    
    allZeros = True
    for j in range(n):
        if mat[i][j]:
            allZeros = False
            break
    
    if allZeros:
        sink.append(i + 1)

for i in range(n):
    
    allZeros = True
    for j in range(n):
        if mat[j][i]:
            allZeros = False
            break
    
    if allZeros:
        source.append(i + 1)

print(len(source), *source)
print(len(sink), *sink)
