class Solution:
    def reverse(self, x: int) -> int:
        temp = str(x)
        result = ''
        if temp[0] == '-':
            result += '-'
            for i in range(len(temp)-1, 0, -1):
                result += temp[i]
        else:
            for i in range(len(temp)-1, -1, -1):
                result += temp[i]
        result = int(result)
        if result >= 2**31 or result < - 2**31:
            return 0
        else:
            return result


sl = Solution()
print(sl.reverse(1534236469))