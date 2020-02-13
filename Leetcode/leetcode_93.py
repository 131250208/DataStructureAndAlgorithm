'''
复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]

思路：
此题时候用递归，定义函数f(s, num)表示将s用"."分割成num段并返回所有符合条件的字符串的list，
则f满足以下递归关系：
f(s, num) = pre_str + "." + f(left_str, num - 1) # pre_str 代表从当前s切割出来的前缀，left_str为切割后剩余子串

结果：28ms通过
'''

class Solution(object):
    def legal_bits(self, bits):
        if len(bits) > 3 or int(bits) > 255 or bits[0] == "0" and len(bits) >= 2:
            return False
        return True

    def get_substr_list(self, s, num):
        if len(s) < num or len(s) > num * 3:
            return []
        if num == 1:
            res = [s, ] if self.legal_bits(s) else []
            return res

        substr_list_total = []
        for i in range(3):
            pre_s = s[:i + 1]
            if not self.legal_bits(pre_s):
                continue
            left_s = s[i + 1:]
            substr_list = self.get_substr_list(left_s, num - 1)
            if len(substr_list) > 0:
                substr_list_total.extend(["{}.{}".format(pre_s, substr) for substr in substr_list])

        return substr_list_total

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.get_substr_list(s, 4)


if __name__ == "__main__":
    sol = Solution()
    print(sol.restoreIpAddresses(""))



