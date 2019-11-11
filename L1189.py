class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        for s in text:
            if s in count.keys():
                count[s] += 1
        return min(count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n'])

text = "nlaebolko"
sl = Solution()
print(sl.maxNumberOfBalloons(text))
