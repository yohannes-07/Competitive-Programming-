class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        chars = path.split("/")
   
        for char in chars:
            if stack and char == "..":
                stack.pop()
                
            elif char not in [".", "", ".."]:
                stack.append(char)
                
        return "/" + "/".join(stack)