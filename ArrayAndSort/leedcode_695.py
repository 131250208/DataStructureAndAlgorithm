'''
岛屿的最大面积

给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。
注意: 给定的矩阵grid 的长度和宽度都不超过 50。

思路：
用递归实现深搜
1. 注意检查边界
2. 注意走过的地方要标0
'''

class Solution(object):
    def go(self, island, ind_i, ind_j):
        if ind_i < 0 or ind_j < 0 or ind_i > len(island) - 1 or ind_j > len(island[0]) - 1 or island[ind_i][ind_j] == 0: #
            return 0

        size_subisland = 0
        island[ind_i][ind_j] = 0
        size_subisland += self.go(island, ind_i + 1, ind_j)
        size_subisland += self.go(island, ind_i - 1, ind_j)
        size_subisland += self.go(island, ind_i, ind_j + 1)
        size_subisland += self.go(island, ind_i, ind_j - 1)
        return size_subisland + 1

    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        max_size = 0
        for ind_i, row in enumerate(grid):
            for ind_j, c in enumerate(row):
                if c == 1:
                    max_size = max(max_size, self.go(grid, ind_i, ind_j))
        return max_size

if __name__ == "__main__":
    sol = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,1,1,0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,1,1,0,0,1,0,1,0,0],
             [0,1,0,0,1,1,0,0,1,1,1,0,0],
             [0,0,0,0,0,0,0,0,0,0,1,0,0],
             [0,0,0,0,0,0,0,1,1,1,0,0,0],
             [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(sol.maxAreaOfIsland(grid))
