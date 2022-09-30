# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
       
        array = []
        ctr = 0
        while curr:
            array.append(curr.val)
            ctr += 1
            curr = curr.next
            
        array.sort()
        dummy = head
        
        for i in range(ctr):
            dummy.val = array[i]
            dummy = dummy.next
            
        return head
    
        