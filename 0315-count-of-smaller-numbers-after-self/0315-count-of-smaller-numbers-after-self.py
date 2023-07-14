class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = []
        res = [0] * len(nums)

        for i, num in enumerate(nums):
            arr.append((num, i))

        def merge(left, right):
            l = 0
            r = 0
            temp = []
            countRightLessThanLeft = 0

            while l < len(left) and r < len(right):
                if left[l][0] > right[r][0]:
                    temp.append(right[r])
                    r += 1
                    countRightLessThanLeft += 1
                else:
                    temp.append(left[l])
                    res[left[l][1]] += countRightLessThanLeft
                    l += 1

            if l < len(left):
                for i in range(l, len(left)):
                    temp.append(left[i])
                    res[left[i][1]] += countRightLessThanLeft

            if r < len(right):
                for i in range(r, len(right)):
                    temp.append(right[i])

            return temp

        def merge_sort(arr):
            if len(arr) == 1:
                return arr

            midIndex = len(arr) // 2
            left_side = merge_sort(arr[:midIndex])
            right_side = merge_sort(arr[midIndex:])

            return merge(left_side, right_side)

        merge_sort(arr)
        return res
