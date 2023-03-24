test_cases = int(input())
for _ in range(test_cases):
    m = int(input())
    arr = list(map(int, input().split()))

    sorted_ = sorted(arr)
    operations = 0

    def mergeSort(left, right, arr):
        if left == right:
            return [arr[left]]

        mid = left + (right - left) // 2
        left_half = mergeSort(left, mid, arr)
        right_half = mergeSort(mid + 1, right, arr)

        return merge(left_half, right_half)

    def merge(left_half, right_half):
        global operations
        res = []

        if left_half[0] <= right_half[0]:
            res.extend(left_half)
            res.extend(right_half)

        else:
            res.extend(right_half)
            res.extend(left_half)
            operations += 1

        return res

    if mergeSort(0, len(arr) - 1, arr) ==  sorted_:
        print(operations)

    else:
        print(-1)
