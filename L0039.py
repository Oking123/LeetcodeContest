from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        pattern1 = []
        pattern2 = []
        for i in range(len(candidates)):
            pattern1.append(0)
            pattern2.append(float('inf'))
        result = [[pattern1]]
        for i in range(target):
            result.append([pattern2[:]])
        for tar in range(target+1):
            for index in range(len(candidates)):
                if tar - candidates[index] >= 0:
                    for temp in result[tar - candidates[index]]:
                        ans = temp[:]
                        ans[index] += 1
                        if ans not in result[tar]:
                            result[tar].append(ans)
        answer = []
        for re in result[target][1:]:
            temp = []
            for index in range(len(candidates)):
                for i in range(re[index]):
                    temp.append(candidates[index])
            answer.append(temp)
        return answer

