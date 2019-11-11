from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        u = upper
        l = lower
        if upper + lower != sum(colsum):
            return []
        result = [[], []]
        for co in colsum:
            if co == 2:
                result[0].append(1)
                result[1].append(1)
                upper -= 1
                lower -= 1
            else:
                result[0].append(0)
                result[1].append(0)

        for index in range(len(colsum)):
            if colsum[index] == 1:
                if upper > 0:
                    result[0][index] = 1
                    upper -= 1
                else:
                    result[1][index] = 1
                    lower -= 1
        if sum(result[0]) == u and sum(result[1]) == l:
            return result
        else:
            return []

