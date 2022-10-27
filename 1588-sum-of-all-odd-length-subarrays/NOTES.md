prefix = []
prefix.append(arr[0])
for i in range(1, len(arr)):
prefix.append(prefix[-1] + arr[i])
summ = 0
for i in range(len(arr)):
for j in range(len(arr)):
if (j - i + 1) % 2 == 1:
if i > 0:
summ += prefix[j] - prefix[i-1]
else:
summ += prefix[j]
return summ