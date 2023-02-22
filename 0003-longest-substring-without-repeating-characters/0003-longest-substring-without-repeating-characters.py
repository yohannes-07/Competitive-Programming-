class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        left = 0
        longest_substring = 0
        n = len(s)
        
        for right in range(n):
            
            while s[right] in unique:
                unique.remove(s[left])
                left += 1
                
            unique.add(s[right])
            longest_substring = max(longest_substring, right - left + 1)
            
        return longest_substring