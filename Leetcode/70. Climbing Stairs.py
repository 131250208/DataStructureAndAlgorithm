class Solution:
    def climbStairs(self, n: int) -> int:
        f = [-1, 1, 2]
        if 1 <= n <= 2:
            return f[n]
        for i in range(3, n + 1):
            f[0] = f[1] + f[2]
            f[1], f[2] = f[2], f[0]
        return f[0]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))