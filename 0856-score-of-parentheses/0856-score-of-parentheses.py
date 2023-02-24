class Solution(object):
    def scoreOfParentheses(self, s):
        stack = []
        score = 0
        
        for char in s :
            
            # whenever we get "("  we push the already calculated score to the stack
            # and set the score to 0 coz we're looking  for new pair
            if char == "(":
                stack.append(score)
                score = 0
                
            # if  ")", we got a pair and the score will be either 1 if it is not nested
            # or 2 * the inside value(score) ..so choos the max as the score 
            #may be set to 0 for non-nested pairs
            else:
                
                score = stack.pop() + max(2 * score, 1)
                
        return score
