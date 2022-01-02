class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        set_sign = False
        res = 0
        int_max = (1 << 31) - 1
        for c in s:
            if c == " " and not set_sign:
                continue
            elif c == "+" and not set_sign:
                sign = 1
                set_sign = True
            elif c == "-" and not set_sign:
                int_max += 1
                sign = -1
                set_sign = True
            elif 0 <= ord(c) - ord("0") <= 9:
                set_sign = True
                new_num = ord(c) - ord("0")
                if res > (int_max - new_num) / 10:
                    return int_max * sign
                res = res * 10 + new_num
            else:
                break

        return res * sign


if __name__ == '__main__':
    s = Solution()
    cases = ["42", "   -42", "4193 with words", "words and 987", "   +0 123", "00000-42a1234", "21474836460", "+-12", "-91283472332"]
    expected = [42, -42, 4193, 0, 0, 0, 2147483647, 0, -2147483648]
    for idx, case in enumerate(cases):
        assert s.myAtoi(case) == expected[idx], "Wrong answer: {} -> {}, e: {}".format(case, s.myAtoi(case), expected[idx])
    print("All cases above passed!")
    # print(s.myAtoi("+-12"))
    # print(ord("9") - ord("0"))
