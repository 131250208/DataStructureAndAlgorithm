class Solution:
    def reverse(self, x: int) -> int:
        rev = 0

        neg = x < 0
        x = - x if neg else x
        int_max = 1 << 31 if neg else (1 << 31) - 1

        while x != 0:
            pop = x % 10
            x //= 10
            # last_digit = int_max % 10 if not neg else int_max % 10 + 1
            # if (rev > int_max / 10 or (rev == int_max / 10 and pop > last_digit)):
            #     return 0
            if rev > (int_max - pop) / 10:
                return 0
            rev = rev * 10 + pop

        return rev if not neg else - rev


if __name__ == '__main__':
    s = Solution()
    print(s.reverse(-123))