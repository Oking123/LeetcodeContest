from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        result = ['0', '1']
        for i in range(n-1):
            temp = result[:]
            temp.reverse()
            result += temp
            for index in range(0, int(len(result)/2)):
                result[index] = '0' + result[index]
            for index in range(int(len(result)/2), len(result)):
                result[index] = '1' + result[index]
        startindex = 0
        for index in range(len(result)):
            result[index] = int(result[index], 2)
            if result[index] == start:
                startindex = index
        return result[startindex:] + result[:startindex]

