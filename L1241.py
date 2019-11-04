class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        ans = 0
        xs = 0
        ys = 0
        for index in range(len(s1)):
            if s1[index] != s2[index]:
                if s1[index] == 'x':
                    xs += 1
                else:
                    ys += 1
        if xs % 2 + ys % 2 == 1:
            return -1
        elif xs % 2 == 1:
            return int(xs/2)+int(ys/2)+2
        else:
            return int(xs/2+ys/2)
