class Solution:
    def sortColors(self, nums: List[int]) -> None:
        redPointer, whitePointer, bluePointer = 0, 0, len(nums) - 1       
        while whitePointer <= bluePointer:

            #if the white pointer  points to red value(0)
            #swap the red pointer value with white pointer value and move  both pointers forward
            
            if nums[whitePointer] == 0:
                nums[redPointer], nums[whitePointer] = nums[whitePointer], nums[redPointer]
                
                whitePointer += 1
                redPointer += 1

            #if the white pointer  points to blue value(2)
            #swap the blue pointer value with white pointer value and move the blue pointer backward
            
            elif nums[whitePointer] == 2:
                nums[whitePointer], nums[bluePointer] = nums[bluePointer], nums[whitePointer]
                bluePointer -= 1

            #if the white pointer points to white value(1)
            # just no need to swap, just move the white pointer forward
            
            else:  
                whitePointer += 1