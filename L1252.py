from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        results = []
        pattern = []
        for i in range(m):
            pattern.append(0)
        for i in range(n):
            results.append(pattern[:])
        for indice in indices:
            for x in range(m):
                results[indice[0]][x] += 1
            for y in range(n):
                results[y][indice[1]] += 1
        ans = 0
        for x in range(m):
            for y in range(n):
                if results[y][x] % 2 == 1:
                    ans += 1
        return ans


indice = [[1, 1], [0, 0]]
sl = Solution()
print(sl.oddCells(2, 2, indice))