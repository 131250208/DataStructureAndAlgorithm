'''
leetcode_236
'''

from Leetcode.nodes import TreeNode


class Operation:
    def __init__(self, op, node):
        self.op = op
        self.node = node


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        '''
        iterative version
        :param root:
        :param p:
        :param q:
        :return:
        '''
        op_stack = []
        data_stack = [] # 储存操作的返回值，记得0操作时需要读1操作的返回值，一定要先弹栈再判断特殊情况返回，不要把不用的参数留在栈里
        op_stack.append(Operation(1, root))
        while len(op_stack):
            opertation = op_stack.pop()
            node = opertation.node

            if opertation.op == 1: # 递归操作, 进行分解
                if node is None:
                    data_stack.append(node)
                    continue
                op_stack.append(Operation(0, node))
                op_stack.append(Operation(1, node.left))
                op_stack.append(Operation(1, node.right))

            elif opertation.op == 0:
                left_selected = data_stack.pop()
                right_selected = data_stack.pop()

                if node is None or node == p or node == q:
                    data_stack.append(node)
                    continue

                if left_selected is not None and right_selected is not None:
                    data_stack.append(node)
                    continue
                if left_selected is not None and right_selected is None:
                    data_stack.append(left_selected)
                else:
                    data_stack.append(right_selected)

        return data_stack.pop()
    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     '''
    #     recursive version
    #     :param root:
    #     :param p:
    #     :param q:
    #     :return:
    #     '''
    #     if root is None or root == q or root == p: # 将找到的目标返回
    #         return root
    #     left_selected = self.lowestCommonAncestor(root.left, p, q)
    #     right_selected = self.lowestCommonAncestor(root.right, p, q)
    #     if left_selected is not None and right_selected is not None: # 如果目标来自两个分支，则该root是LCA
    #         return root
    #     # 如果目标来自其中一个分支，则返回那个分支找到的目标，这一句既包括只找到p或者q的情况，又包括在之前已经找到root的情况
    #     return left_selected if left_selected else right_selected


if __name__ == "__main__":
    tl = TreeNode(5)
    tr = TreeNode(1)
    root = TreeNode(3)
    root.right = tr
    root.left = tl
    sol = Solution()
    print(sol.lowestCommonAncestor(root, tl, tr))


