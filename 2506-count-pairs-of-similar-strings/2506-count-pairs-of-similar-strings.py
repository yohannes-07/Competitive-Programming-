import math
class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dic = {}
        for word in words:
            word = set(word)
            word = list(word)
            word = sorted(word)
            word = "".join(word)
            print(word)
            if word in dic:
                dic[word] += 1
            else:
                 dic[word] = 1
        print(dic)
        ans = 0
        for value in dic.values():
            if value == 1:
                continue
            else:
                comb = (math.factorial(value))/(math.factorial(value - 2) * 2)
                ans += int(comb)
        return ans