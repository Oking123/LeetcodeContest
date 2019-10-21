class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        if n == 2:
            return '11'
        result = '11'
        for i in range(n-2):
            count = 1
            temp = ''
            for index in range(0, len(result)):
                if index == len(result) - 1:
                    temp += str(count)
                    temp += str(result[index])
                elif result[index] != result[index+1]:
                    temp += str(count)
                    temp += str(result[index])
                    count = 1
                else:
                    count += 1
            result = temp
        return result

sl = Solution()
print(sl.countAndSay(6))
