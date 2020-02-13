class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(pre) == 0 or len(tin) == 0:
            return None

        for ind, v in enumerate(tin):
            if v == pre[0]:
                root = TreeNode(pre[0])
                root.left = self.reConstructBinaryTree(pre[1:1 + ind], tin[:ind])
                root.right = self.reConstructBinaryTree(pre[1 + ind:], tin[ind + 1:])
                return root
