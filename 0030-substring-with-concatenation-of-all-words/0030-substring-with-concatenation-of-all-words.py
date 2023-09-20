from itertools import permutations
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        def check_presence(i):
            WC = collections.Counter(words)
            words_found = 0

            for j in range(i, i+size, words_len):
                sub = s[j:j+words_len]
                if WC[sub] > 0:
                    WC[sub] -= 1
                    words_found += 1
                else:
                    break
            return words_found == n_words

        n = len(s)
        words_len = len(words[0])
        n_words = len(words)
        size = words_len * n_words
        res=[]
        
        for i in range(n- size + 1):
            if check_presence(i):
                res.append(i)
        return res