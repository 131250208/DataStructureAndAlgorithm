class Solution:
    def _search(self, stack, op, n, current_str):
        '''
        op: operation 0 = pop, 1 = append
        '''
        stack = stack[:]
        current_str = current_str[:]

        # 剪枝
        if op == 1 and n == 0:
            return
        if op == 0 and len(stack) == 0:
            return

        # 执行出栈或者入栈操作
        if op:
            n -= 1
            stack.append("(")
            current_str += "("
        else:
            stack.pop()
            current_str += ")"

        # 检查叶子：终止存储结果
        if len(stack) == 0 and n == 0:
            self.res.append(current_str)
            return

        # 生长
        self._search(stack, 1, n, current_str)
        self._search(stack, 0, n, current_str)

    def generateParenthesis(self, n: int):
        self.res = []
        self._search([], 1, n, "")
        return self.res


if __name__ == "__main__":
    sol = Solution()
    print(sol.generateParenthesis(3))

