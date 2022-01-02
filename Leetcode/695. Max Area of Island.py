from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_valid(i, j):
            return 0 <= i <= len(grid) - 1 and 0 <= j <= len(grid[0]) - 1 and grid[i][j] == 1

        def sink(i, j):
            area = 0
            if is_valid(i, j):
                grid[i][j] = 0
                area += 1
                for d in dirs:
                    area += sink(i + d[0], j + d[1])
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    max_area = max(max_area, sink(i, j))
        return max_area

if __name__ == "__main__":
    s = Solution()
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(s.maxAreaOfIsland(grid))
    print(s.maxAreaOfIsland([[0, 0, 0, 0, 0, 0, 0, 0]]))
