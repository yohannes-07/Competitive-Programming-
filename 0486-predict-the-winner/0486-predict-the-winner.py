class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def winner(nums, start, end, turn):
            
            if start == end:
                return nums[start] * turn

            a = nums[start] * turn + winner(nums, start+1, end, -turn)
            b = nums[end] * turn + winner(nums, start, end-1, -turn)
    
            return max(a*turn, b*turn) * turn

        score =  winner(nums, 0, len(nums)-1, 1)
        
        return score >= 0