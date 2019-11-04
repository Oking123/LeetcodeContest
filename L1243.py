class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sym = 0
        ans = ''
        temp = [-1]
        for index in range(len(s)):
            if s[index] == '(':
                temp.append(index)
                sym += 1
            elif s[index] == ')':
                if sym > 0:
                    sym -= 1
                    temp.pop()
                else:
                    temp.append(index)
        temp.append(len(s))
        for index in range(len(temp)-1):
            ans += s[temp[index]+1:temp[index+1]]
        return ans