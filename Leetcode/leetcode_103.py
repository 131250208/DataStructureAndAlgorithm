'''
leetcode_103 Binary Tree Zigzag Level Order Traversal

思路：1 queue and 1 stack
'''
from Others.nodes import TreeNode
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        que = deque([])
        stack = []
        res = []
        que.append(root)
        while True:
            res_que = []
            while len(que):
                node = que.pop()
                if node:
                    res_que.append(node.val)
                    stack.append(node.left)
                    stack.append(node.right)
            if len(res_que) == 0:
                break
            res.append(res_que)

            res_stack = []
            while len(stack):
                node = stack.pop()
                if node:
                    res_stack.append(node.val)
                    que.append(node.left)
                    que.append(node.right)
            if len(res_stack) == 0:
                break
            res.append(res_stack)

        return res
