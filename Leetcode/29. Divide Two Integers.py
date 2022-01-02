class Solution:
    def divide_positive(self, dividend: int, divisor: int) -> int:
        divisor_agent = divisor
        shift = 0
        while dividend >= divisor_agent << 1:
            divisor_agent = divisor_agent << 1
            shift += 1

        quotient = 1 << shift
        if dividend - divisor_agent >= divisor:
            quotient += self.divide(dividend - divisor_agent, divisor)

        return quotient

    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == - 1 << 31 and divisor == -1:
            return (1 << 31) - 1

        sign = 1 if dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        if dividend >= divisor:
            quotient = self.divide_positive(dividend, divisor)
        else:
            quotient = 0

        return quotient * sign

if __name__ == "__main__":
    s = Solution()
    print(s.divide(10, 3))
    print(s.divide(2147483647, 1))
    print(s.divide(-2147483648, -1))