class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        if "." in queryIP:
            ip_parts = queryIP.split(".")
            
            if len(ip_parts) != 4:
                return "Neither"
            
            for part in ip_parts:
                if not part.isdigit() or (len(part) > 1 and part[0] == '0') or not (0 <= int(part) <= 255):
                    return "Neither"
                
            return "IPv4"
        
        elif ":" in queryIP:
            ip_parts = queryIP.split(":")
            
            if len(ip_parts) != 8:
                return "Neither"
            
            valid_letters = set("0123456789ABCDEFabcdef")
            for part in ip_parts:
                if len(part) == 0 or len(part) > 4 or not all(c in valid_letters for c in part):
                    return "Neither"
                
            return "IPv6"
        
        return "Neither"
