class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
    #backtrack with bitwise   
        res = []

        usedElem = 0
        def backtrack(i, acc):
            
            nonlocal usedElem
            if i >= len(nums):
                res.append(acc[:])
                return

            for idx in range(len(nums)):

                #check it hasn't been used in the current permutaion
                if usedElem & (1 << idx) == 0:

                    #turn on to indicate it has been used in the current permutaion
                    usedElem |= (1 << idx)

                    acc.append(nums[idx])
                    backtrack(i + 1, acc)

                    acc.pop()

                    #turn off the usedElem to use it in other permutaion
                    usedElem ^= (1 << idx)

        backtrack(0, [])
        return res


