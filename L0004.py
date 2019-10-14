from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def divide(nums1, nums2):
            if not nums1:
                nums1 = nums2
                return
            


sl = Solution()
A = [1,2,4,6,7,8]
B = []
print(sl.findMedianSortedArrays(A, B))