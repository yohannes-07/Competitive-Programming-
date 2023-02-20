# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashSet = {}
        curr = head
        
        while curr:
            if curr in hashSet:
                print(hashSet)
                return True
            
            hashSet[curr] = 1
            curr = curr.next
            
        return  False