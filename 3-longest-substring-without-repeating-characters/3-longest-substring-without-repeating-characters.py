class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dict=set()

        left=0 

        max_len = 0 

        for i in range(len(s)):

            while s[i] in dict:

                dict.remove(s[left])

                left +=1

            dict.add(s[i])

            max_len =max(max_len,i-left+1)

        return max_len
        
     
       
        