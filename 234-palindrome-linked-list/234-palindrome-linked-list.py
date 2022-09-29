# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head
        if not head:
            return True
        return self.helper(head)
    
    def helper(self, right):
        
        if not right:
            return True
        ans = self.helper(right.next) and right.val == self.left.val
        
        self.left = self.left.next
        return ans