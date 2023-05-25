class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dic = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                dic[bill] += 1
                
            elif bill == 10:
                if 5 in dic:
                    dic[5] -= 1
                    dic[10] += 1
                    
                    if dic[5] == 0:
                        dic.pop(5)
                        
                else:
                    return False
                
            else:
               
                if 5 in dic and 10 in dic:
                    dic[5] -= 1
                    dic[10] -= 1
                
                elif 5 in dic:
                    if dic[5] >= 3:
                        dic[5] -= 3
                        
                    else:
                       
                        return False
                    
                else: return False
                
                if dic[5] == 0:
                    dic.pop(5)
                if dic[10] == 0:
                    dic.pop(10)
          
            print(dic)
        return True