import math
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dic = {}
        for word in words:
            
            #convert eache word to set so that no duplicated letters
            #change the set to list to sort elemnts and 
            #change it to string to make ur key hashable(immutabel)
            
            word = list(set(word))
            word = sorted(word)
            word = "".join(word)
         
            if word in dic:
                dic[word] += 1
                
            else:
                 dic[word] = 1
   
        # iterate through the dic value and find no of pairs of similar strings
        # use combination rule to find no of pairs => c(n, p) = n!/((n-p)! * p!)
        #p is 2 in this problem
        
        ans = 0
        for value in dic.values():
            if value == 1:
                continue
                
            else:
                comb = (math.factorial(value))/(math.factorial(value - 2) * 2)
                ans += int(comb)
                
        return ans