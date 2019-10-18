from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        temp = nums[-1]
        for index in range(len(nums)-2, -1, -1):
            if nums[index] == temp:
                temp = nums[index]
                nums.remove(nums[index])
            temp = nums[index]
        return len(nums)


sl = Solution()
A = [1,1,1,1,1,2,2,3]
print(sl.removeDuplicates(A))
print(A)
