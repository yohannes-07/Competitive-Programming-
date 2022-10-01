class Solution(object):
    def totalFruit(self, fruits):
        fypes = Counter()
        new = ans = right = left = 0
        
        for right in range(len(fruits)):
            if fypes[fruits[right]] == 0:
                new += 1

            fypes[fruits[right]] += 1

            while new > 2:
                fypes[fruits[left]] -= 1
                if fypes[fruits[left]] == 0:

                    new -= 1

                left += 1
            ans = max(ans, right-left+1)
        
        return ans
      
  
        
        