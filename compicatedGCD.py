a, b = list(input().split())

len1 = len(a)
len2 = len(b)

if len1 < len2:
    print("1")
else:
    for i in range(len1):
        if a[i] != b[i]:
            print("1")
            break
    else:
        print(a)
