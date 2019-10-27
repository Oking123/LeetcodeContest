"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""


class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        pass



from typing import List


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        result = []
        x, y = 1, 1000
        while y >= x:
            if customfunction.f(x, y) == z:
                result.append([x, y])
                y -= 1
            elif customfunction.f(x, y) > z:
                y -= 1
            else:
                x += 1
        x, y = 1000, 1
        while x > y:
            if customfunction.f(x, y) == z:
                result.append([x, y])
                x -= 1
            elif customfunction.f(x, y) > z:
                x -= 1
            else:
                y += 1
        return result
