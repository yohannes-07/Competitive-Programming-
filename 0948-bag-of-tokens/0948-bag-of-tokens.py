class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = score = res = 0
        right = len(tokens) -1
        while left <= right:
            
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                res = res= max(res, score)
                
            elif score >= 1:
                
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        return res