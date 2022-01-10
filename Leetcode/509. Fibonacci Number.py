class Solution:
    def fib(self, n: int) -> int:
        f = [0, 1, -1]
        if n <= 1:
            return f[n]

        for i in range(2, n + 1):
            f[2] = f[0] + f[1]
            f[0], f[1] = f[1], f[2]

        return f[2]


if __name__ == "__main__":
    s = Solution()
    print(s.fib(4))