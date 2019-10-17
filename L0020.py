class Solution:
    def isValid(self, s: str) -> bool:
        temp = list()
        for i in s:
            if i == '(' or i == '[' or i == '{':
                temp.append(i)
            elif not temp:
                return False
            elif i == ')' and temp.pop() != '(':
                return False
            elif i == ']' and temp.pop() != '[':
                return False
            elif i == '}' and temp.pop() != '{':
                return False
        return temp == []

