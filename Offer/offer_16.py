class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0.0:
            return 0.0
        if exponent == 0:
            return 1.0

        def power_abs_exp(b, abs_exp):
            if abs_exp == 0:
                return 1
            if abs_exp == 1:
                return b
            result = power_abs_exp(b, abs_exp >> 1)
            result *= result
            if abs_exp & 0x1:
                result *= b
            return result

        if exponent > 0:
            return power_abs_exp(base, exponent)
        elif exponent < 0:
            return 1 / power_abs_exp(base, - exponent)


if __name__ == "__main__":
    s = Solution()
    print(s.Power(2.0, 3))