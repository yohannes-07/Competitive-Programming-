class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        added = ""
        
        for ch in path + "/":
            if ch == "/":
                if added == "..":
                    if stack:
                        stack.pop()
                elif added and added != ".":
                    stack.append(added)
                added = ""
                
            else:
                added += ch
                
        return "/" + "/".join(stack)
                