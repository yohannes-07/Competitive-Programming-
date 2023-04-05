class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        # two sets are needed: 'one' and 'two'
        # Dry run
        
        # First Appearance : one will have two will not
        # Second Appearance : one will remove and two will add
        # Third Appearance: one will not able to add as it is there in two
        # and two will remove because it was there.   
        # So one will have only which has occurred once and two will not have anything
        
        one = 0
        two = 0
        
        for num in nums:
            
            # if one has a number already remove it, and it does not have that number
            # appeared previously and it is not there in 2 then add it in one.
            one = (one ^ num) & ~two
            
            # if two has a number already remove it, and it does not have that number
            # appeared previously and it is not there in 1 then add it in two.
            
            two = (two ^ num) & ~one
            
        return one
        