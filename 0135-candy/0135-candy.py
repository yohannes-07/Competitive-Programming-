class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        left_to_right = [1] * n
        right_to_left = [1] * n
        candies = [1] * n
        
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left_to_right[i] += left_to_right[i-1]
                candies[i] = max(right_to_left[i],left_to_right[i] )
                
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_to_left[i] += right_to_left[i + 1] 
                candies[i] = max(right_to_left[i],left_to_right[i] )
                
     
        return sum(candies)