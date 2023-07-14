class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr = [(num, i) for i, num in enumerate(nums)]
        res = [0] * len(nums)

        def merge_sort(arr):
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)

        def merge(left, right):
            merged = []
            i, j = 0, 0
            count_right_less_than_left = 0

            while i < len(left) and j < len(right):
                if left[i][0] > right[j][0]:
                    merged.append(right[j])
                    count_right_less_than_left += 1
                    j += 1
                else:
                    merged.append(left[i])
                    res[left[i][1]] += count_right_less_than_left
                    i += 1

            while i < len(left):
                merged.append(left[i])
                res[left[i][1]] += count_right_less_than_left
                i += 1

            while j < len(right):
                merged.append(right[j])
                j += 1

            return merged

        merge_sort(arr)
        return res
