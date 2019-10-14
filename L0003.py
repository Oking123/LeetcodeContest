class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        temp = ''
        for i in s:
            if i not in temp:
                temp += i
                result = max(result, len(temp))
            else:
                while True:
                    if temp[0] == i:
                        temp = temp[1:]
                        break
                    temp = temp[1:]
                temp += i
        return result


ls = Solution()
print(ls.lengthOfLongestSubstring("aabaab!basdasdb"))
