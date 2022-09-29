# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        self.left = head
        self.out = 0
        return self.helper(head)
    
    def helper(self, right):
        
        if not right:
            return True
        ans = self.helper(right.next) and right.val + self.left.val
        self.out = max(self.out, ans)
      
        self.left = self.left.next
        return self.out