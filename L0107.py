# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        layor = [root]
        values = [root.val]
        ans = [values[:]]
        while layor:
            temp = []
            values = []
            for node in layor:
                if node.left is not None:
                    temp.append(node.left)
                    values.append(node.left.val)
                if node.right is not None:
                    temp.append(node.right)
                    values.append(node.right.val)
            layor = temp[:]
            if layor:
                ans.insert(0, values[:])
        return ans
