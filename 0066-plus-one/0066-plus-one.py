class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = "".join(list(map(str, digits)))
        num = int(num) + 1
        
        return [int(digit) for digit in str(num)]