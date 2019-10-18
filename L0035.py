from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binarysearch(nums, p, r, target):
            if p == r-1 or p == r:
                if nums[p] >= target:
                    return p
                elif nums[p] < target <= nums[r]:
                    return r
                else:
                    return r+1
            median = int((p+r)/2)
            if nums[median] < target:
                return binarysearch(nums, median, r, target)
            elif nums[median] > target:
                return binarysearch(nums, p, median, target)
            else:
                return median

        return binarysearch(nums, 0, len(nums)-1, target)