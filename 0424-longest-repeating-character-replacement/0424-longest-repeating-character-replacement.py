class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = longest_substring = most_freq = 0
        chars_freq = defaultdict(int)
        
        for i in range(len(s)):
            chars_freq[s[i]] += 1
            most_freq = max(most_freq, chars_freq[s[i]])
            
            # longest substring - most frequent char <= k if the formula is valid
            # it means we get the longest substring with operations <= k
            # as the most freq char makes the longest substring
            
            #if invalid window, subtract the left most elem from it
            if i - left + 1 - most_freq > k:
                chars_freq[s[left]] -= 1
                left += 1
            
                
            longest_substring = max(longest_substring,  i - left + 1)
                
                
        return longest_substring