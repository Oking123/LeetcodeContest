from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans = 0
        odds = []
        temp = 1
        for num in nums:
            if num % 2 == 0:
                temp += 1
            else:
                odds.append(temp)
                temp = 1
        odds.append(temp)
        if len(odds) <= k:
            return 0
        else:
            for index in range(k, len(odds)):
                ans += odds[index-k] * odds[index]
        return ans


