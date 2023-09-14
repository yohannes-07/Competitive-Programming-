class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        
        i = 0
        width = 0
        curr_line = []
        
        while i < len(words):
            curr_word = words[i]
            
            if width + len(curr_word) <= maxWidth:
                curr_line.append(curr_word)
                width += len(curr_word) + 1
                i += 1
            
            else:
                spaces = maxWidth - width + len(curr_line)
                added = 0
                j = 0
                
                while added < spaces:
                    if j >= len(curr_line) - 1:
                        j = 0
                    
                    curr_line[j] += " "
                    
                    added += 1
                    j += 1
                    
                    
                res.append("".join(curr_line))
                curr_line = []
                width = 0
                
        for word  in range(len(curr_line) - 1):
            curr_line[word] += " "
            
        curr_line[-1] += " " * (maxWidth - width + 1)
        res.append("".join(curr_line))
        
        return res
                    
                
        