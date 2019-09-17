class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        num_reversed = 0
        while x:
            n = x % 10
            num_reversed = num_reversed * 10 + n
            x = x // 10

        if num_reversed == x:
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    num = 121
    print(sol.isPalindrome(num))
