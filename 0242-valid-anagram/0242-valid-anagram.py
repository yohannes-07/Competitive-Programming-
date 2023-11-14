class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = Counter(s)
        
        for char in t:
            if char in s_counter:
                s_counter[char] -= 1
                if s_counter[char] == 0:
                    s_counter.pop(char)
            else:
                s_counter[char] = s_counter.get(char, 0) + 1
                    
        if not s_counter:
            return True
        
        return False