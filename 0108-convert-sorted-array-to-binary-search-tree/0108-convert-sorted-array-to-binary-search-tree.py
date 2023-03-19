# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums) - 1
       
        def helper(left, right):
            
            if left > right:
                return
            
            mid = left + (right - left)//2
            
            root = TreeNode(nums[mid])
            
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root

        return  helper(left, right)
