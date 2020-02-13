'''
第k个排列

给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。
按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：
"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：
给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

示例 1:
输入: n = 3, k = 3
输出: "213"

示例 2:
输入: n = 4, k = 9
输出: "2314"

思路一：
递归进行全排列
结果超时

思路二：
1. 根据数所处的位置k，可以一步步推出选择排列的数字
2. 最终的排列结果的第i个数与n-i的排列可能性个数有关（即(n-1)!）。
3. 其实可以假设所有的排列结果已经计算好，将它们按开头数字递归地分块。
    e.g.
    "123"  ->  "23"
    "132"       --
               "32"
     ---
    "213"
    "231"
     ---
    "312"
    "321"

4. 第i层的块大小为(n-i)!，所以， 计算1~n-1的factorial（阶乘），存成数组

例如：
n = 3, k = 3
n_list = [1, 2, 3]
factorial = [1, 2]
factorial 从弹出栈尾（n-i的阶乘个数）
math.ceil(k / 2) = 2，表示数字位于第一层的第二块，在编程时需要再减一作为访问下标。
于是按未排列数字的顺序弹出第二位数字2
不断循环这个过程，直至确定所有的数字，不要遗漏最后一个数字。

结果56ms通过
'''

import math
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        factorial = []
        pre = 1
        for i in range(n - 1):
            current = (i + 1) * pre
            factorial.append(current)
            pre = current

        res = ""
        n_list = [i + 1 for i in range(n)]
        while len(factorial) != 0:
            block_size = factorial.pop()
            block_n = math.ceil(k / block_size) - 1 # 要上取整再减1，因为整除的情况下，如果下取整，则会去到下一个区间，实则应该返回末尾值
            res = "{}{}".format(res, n_list.pop(block_n))
            k = k % block_size

        return "{}{}".format(res, n_list.pop(0))


if __name__ == "__main__":
    sol = Solution()
    print(sol.getPermutation(3, 3))
