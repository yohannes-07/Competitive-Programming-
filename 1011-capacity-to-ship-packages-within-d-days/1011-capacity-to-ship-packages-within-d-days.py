class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def countDays(weight):
            days = 0
            i = 0
            while i < len(weights):
                _sum = 0
                while i < len(weights) and _sum + weights[i] <= weight:
                    _sum += weights[i]
                    i += 1
                days += 1
            return days

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = left + (right - left)//2
            if countDays(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
        return left






        