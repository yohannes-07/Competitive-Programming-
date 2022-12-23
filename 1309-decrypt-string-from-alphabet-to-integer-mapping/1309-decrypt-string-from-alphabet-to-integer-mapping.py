class Solution:
    def freqAlphabets(self, s: str) -> str:
        #dictionary to store numbers as key and charachters as value {"1": "a", "2", "b"..}
        dic = {}
        
        char = "a"
        for i in range(1, 27):
            
            dic[str(i)] = char
            char = chr(ord(char) + 1)
       
        i = len(s) - 1
        output = ""
        
        while i >= 0:
            if s[i] == "#":
                # store the number starting from s[i-1] towards left for tow digits
                i -= 1
                temp = ""
                
                for j in range(2):
                    temp += s[i]
                    i -= 1
                #search the number in dic and add it to the output
                output += dic[temp[::-1]]
            else:
                output += dic[s[i]]
                i -= 1
                
        # reverse the output as it is iterated from right to left
        return output[::-1]
                
        
       