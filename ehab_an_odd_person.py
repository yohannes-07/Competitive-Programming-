n=int(input())
arr= list(map(int, input().split()))

even,odd=False,False

# only odd + even = odd

for i in range(len(arr)):
    if(arr[i]%2==0):
        even=True
    else:
        odd=True


if even and odd:
    arr.sort()

for num in arr:
    print(num,end=" ")
