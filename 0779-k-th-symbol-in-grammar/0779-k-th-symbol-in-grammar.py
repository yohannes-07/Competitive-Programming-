class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0

        # size of each row doubles, so if row 3 has 4 chars, the end idx of that row 
        # will be 2**(1) == 2
        first_half_end_pos = 2**(n - 2)

        # if k is in the first half of the str recurse down a row 
        # if k isn't in the first half of the str, recurse down a row and find the opposite 
        # char's position in the first half
        if k <= first_half_end_pos:
            return self.kthGrammar(n - 1, k)
        else:
            char_in_half_opposite_of_answer = self.kthGrammar(n - 1, k - first_half_end_pos)
            return 1 if char_in_half_opposite_of_answer == 0 else 0