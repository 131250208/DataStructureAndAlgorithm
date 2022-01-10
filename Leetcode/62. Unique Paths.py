class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[1 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    continue
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]

if __name__ == "__main__":
    s = Solution()
    print(s.uniquePaths(3, 7))