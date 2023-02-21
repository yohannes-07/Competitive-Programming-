# Definition for singly-linked list.
class ListNode(object):
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        curr = dummy = ListNode()
        rem = 0
        
        while l1 or l2 or rem:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
                
            if l2:
                val2 =  l2.val
            else:
                val2 = 0
                
            res  = val1 + val2 + rem 
            rem = res // 10
            res = res % 10
            
            curr.next = ListNode(res)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2= l2.next if l2 else None
            
        if rem > 0:
            curr.next = ListNode(rem)
            
        return   dummy.next 
            
            

 
        
    
      
    
        
        