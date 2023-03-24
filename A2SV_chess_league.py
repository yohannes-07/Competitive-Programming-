n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))

def mergeSort(left, right, arr):
        if left == right:
            return [left]

        mid = left + (right - left) // 2
        left_half = mergeSort(left, mid, arr)
        right_half = mergeSort(mid + 1, right, arr)

        return merge(left_half, right_half)

def merge(left, right):
      
    merged = []
    l_ptr = r_ptr = 0
    left_min, right_min = arr[left[0]], arr[right[0]]

    while l_ptr < len(left) and r_ptr < len(right):
        if arr[left[l_ptr]] <= arr[right[r_ptr]]:
            if right_min - arr[left[l_ptr]] <= k:
                merged.append(left[l_ptr])
            l_ptr += 1
        else:
            if left_min - arr[right[r_ptr]] <= k:
                merged.append(right[r_ptr])
            r_ptr += 1

    
    while l_ptr < len(left) and right_min - arr[left[l_ptr]] <= k:
        merged.append(left[l_ptr])
        l_ptr += 1

    while r_ptr < len(right) and left_min - arr[right[r_ptr]] <= k:
        merged.append(right[r_ptr])
        r_ptr += 1

    
    return merged

res = mergeSort(0, 2**n-1 , arr)
for num in sorted(res):
    print(str(num + 1), end=" ")

print()

       

    
