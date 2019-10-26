# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        root.val = 1
        queue = [root]
        result = 0
        while queue:
            root = queue.pop()
            result = max(root.val, result)
            if root.left is not None:
                root.left.val = root.val + 1
                queue.append(root.left)
            if root.right is not None:
                root.right.val = root.val + 1
                queue.append(root.right)
        return result

