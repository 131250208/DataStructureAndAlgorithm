# -*- coding:utf-8 -*-
from Others.nodes import TreeNode
from Others.nodes import buildATree

class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.route = []
        self.routeList = []

    def _FindPath(self, root, expectNumber):
        # write code here
        self.route.append(root.val)

        if root.left is not None: # * is None
            self._FindPath(root.left, expectNumber - root.val)
        if root.right is not None: # * is None
            self._FindPath(root.right, expectNumber - root.val)

        if root.val == expectNumber:
            self.routeList.append(self.route[:])
        # 回溯
        self.route.pop()

    def FindPath(self, root, expectNumber):
        self._FindPath(root, expectNumber)
        return self.routeList

if __name__ == "__main__":
    tr = buildATree([10, 5, 12, 4, 7])
    s = Solution()
    print s.FindPath(tr, 22)