from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def find(num1, num2):
            num1, num2 = max(num1,num2), min(num1, num2)
            while num2 != 0:
                temp = num2
                num2 = num1 % num2
                num1 = temp
            return num1
        hasodd = False
        minnum = nums[0]
        for num in nums:
            if num % 2 == 1:
                hasodd = True
            minnum = min(find(minnum, num), minnum)
            if minnum == 1:
                return True
        return False


