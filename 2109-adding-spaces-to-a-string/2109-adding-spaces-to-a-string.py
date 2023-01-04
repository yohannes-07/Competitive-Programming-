from collections import Counter
class Solution:
   
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        length_of_str = len(s)
       
        #keep all indexes of white spaces in dictionary so that looking up them will be o(1)
        white_space_idxes = Counter(spaces)
        modified_str = ""
       
        #if the index of the given string s is equal to some white space index
        #add space and the char of that index else just add the chars in the new string
        for idx in range(length_of_str):
            if idx in white_space_idxes:
                 modified_str  += " " + s[idx]
               
            else:
                 modified_str  += s[idx]
            
        return  modified_str 