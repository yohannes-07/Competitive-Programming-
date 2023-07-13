class Solution:
    def recurse(self, index, state):
            if index == len(self.nums):
                return 0
            
            if index in self.memo:
                return self.memo[index]
            
            ans = 1
            
            for i in range(index + 1, len(self.nums)):
                if state == 'positive' and self.nums[i] - self.nums[index] < 0:
                    ans = max(ans, 1 + self.recurse(i, 'negative'))
                    
                elif state == 'negative' and self.nums[i] - self.nums[index] > 0:
                    ans = max(ans, 1 + self.recurse(i, 'positive'))
            
            self.memo[index] = ans
            return self.memo[index]
        
    def wiggleMaxLength(self, nums: List[int]) -> int:
        self.memo, res = {}, 1
        self.nums = nums
        
        for i in range(1, len(nums)):
            if self.nums[i] - self.nums[i - 1] > 0:
                res = max(res, 1 + self.recurse(i, 'positive'))
                
            elif self.nums[i] - self.nums[i - 1] < 0:
                res = max(res, 1 + self.recurse(i, 'negative'))
       
        return res