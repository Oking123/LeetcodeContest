from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def unique(str1, str2):
            result = set(str1+str2)
            return len(result) == len(str1)+len(str2)
        result = []
        for ar in arr:
            if len(ar) == len(set(ar)):
                result.append(ar)
            for re in result:
                if unique(ar, re):
                    result.append(ar+re)
        print(result)
        ans = 0
        for resu in result:
            ans = max(ans, len(resu))
        return ans


sl = Solution()
arr = ["cha","r","act","ers"]
print(sl.maxLength(arr))

