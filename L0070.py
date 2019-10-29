from math import factorial

class Solution:
    def climbStairs(self, n: int) -> int:
        ans = 0
        for i in range(0, int(n/2)+1):
            ans += factorial(n-i)/(factorial(n-2*i)*(factorial(i)))
        return int(ans)

sl = Solution()
print(sl.climbStairs(2))