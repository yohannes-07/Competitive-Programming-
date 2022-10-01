class Solution(object):
    def compress(self, chars):
        i = slow =  0 
        while i < len(chars):
            left = i 
            while i + 1 < len(chars) and chars[i] == chars[i+1]:

                i += 1
            num = i - left + 1

            if num > 1:
                chars[slow] = chars[i]
                slow += 1

                for j in range(len(str(num))):
                    chars[slow] = str(num)[j]
                    slow += 1

            else:
                chars[slow] = chars[i]
                slow += 1

            i += 1

        return slow
        
       
       
   
        