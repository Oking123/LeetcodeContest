from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = ''
        for i in digits:
            temp += str(i)
        return list(str(int(temp)+1))

sl = Solution()
A = [1,2,3]
print(sl.plusOne(A))
