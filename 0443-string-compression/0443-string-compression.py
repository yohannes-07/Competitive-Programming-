class Solution(object):
    def compress(self, chars):
        fast, slow = 0, 0
    
        while fast < len(chars):
            x = chars[fast]
            count = 0

            #check if their are same consecutive elems
            #increase the frequency of that elem and the pointer
            while fast < len(chars) and chars[fast] == x:
                fast += 1
                count += 1
            
            chars[slow] = x
            slow += 1

            #add the freq of the elem char by char at the end of the elem
            if count > 1:
                for c in str(count):
                    chars[slow] = c
                    slow += 1

        return slow