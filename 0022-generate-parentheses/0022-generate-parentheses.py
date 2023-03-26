class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(opening, closing, curr):
            
            if (closing < opening or
                opening < 0 or
                closing < 0):
                return
            
            if not opening and not closing:
                res.append(curr)
                return
            
            backtrack(opening - 1, closing, curr + "(")
            backtrack(opening, closing - 1, curr + ")")
            
        
        backtrack(n, n, "")
        return res