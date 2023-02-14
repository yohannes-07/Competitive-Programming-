class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        newRow, newCol=[], []
        count=0

        if len(original)>m*n or len(original)<m*n:
            return []

        for i in original:
            newCol.append(i)
            count+=1

            if count==n:
                newRow.append(newCol)
                newCol=[]
                count=0

        return newRow