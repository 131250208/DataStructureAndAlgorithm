# -*- encoding:utf-8 -*-
'''
leetcode_144 Binary Tree Preorder Traversal
典型递归转迭代的解法
recursive solution -> iterative solution

结果：通过
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Operation:
    def __init__(self, operation, node):
        self.operation = operation # 0 是输出，1 是递归
        self.node = node

class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = []

        stack.append(Operation(1, root))
        while len(stack) != 0:
            operation = stack.pop()
            node = operation.node
            if node is None:
                continue
            if operation.operation == 1: # 改变前中后序只需要改这里
                stack.append(Operation(1, node.right))
                stack.append(Operation(1, node.left))
                stack.append(Operation(0, node))
            elif operation.operation == 0:
                res.append(node.val)

        return res
