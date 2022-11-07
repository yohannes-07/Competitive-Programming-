class Solution:
    def rearrangeArray(self, A: List[int]) -> List[int]:
        A.sort()
        for i in range(1, len(A), 2):
            A[i], A[i - 1] = A[i - 1], A[i]
        print(A)
        return A
