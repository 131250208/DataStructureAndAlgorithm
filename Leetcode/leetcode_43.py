'''
字符串相乘

给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

num1 和 num2 的长度小于110。
num1 和 num2 只包含数字 0-9。
num1 和 num2 均不以零开头，除非是数字 0 本身。
不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

思路一：
实现大整数相乘需要的所有组件，并按乘法的人类计算流程（竖式计算）进行：
单位相加
大整数相加
单位相乘
大整数相乘
结果通过，时间1s左右

思路二：

'''


class Solution:
    def multiply_1bit(self, num1, num2, c):
        '''
        单位相乘
        :param num1: str
        :param num2: str
        :param c: 进位数， int
        :return:
        '''
        num1 = ord(num1) - ord("0")
        num2 = ord(num2) - ord("0")
        res = num1 * num2 + c
        return res // 10, str(res % 10)

    def add_1bit(self, num1, num2, c):
        '''
        单位相加
        :param num1:
        :param num2:
        :param c: 进位
        :return:
        '''
        num1 = ord(num1) - ord("0")
        num2 = ord(num2) - ord("0")
        res = num1 + num2 + c
        return res // 10, str(res % 10)

    def add(self, num1, num2):
        '''
        大整数加法
        :param num1:
        :param num2:
        :return:
        '''
        if len(num1) > len(num2):
            num2 = "0" * (len(num1) - len(num2)) + num2
        elif len(num1) < len(num2):
            num1 = "0" * (len(num2) - len(num1)) + num1

        res = ""
        c = 0
        ind_end = len(num1) - 1
        for i in range(len(num1)):
            c, p = self.add_1bit(num1[ind_end - i], num2[ind_end - i], c)
            res = p + res

        if c != 0:
            res = str(c) + res
        return res

    def multiply(self, num1: 'str', num2: 'str') -> 'str':
        '''
        大整数乘法
        :param num1:
        :param num2:
        :return:
        '''
        if len(num1) > len(num2):
            num2 = "0" * (len(num1) - len(num2)) + num2
        elif len(num1) < len(num2):
            num1 = "0" * (len(num2) - len(num1)) + num1

        res = "0"
        ind_end = len(num1) - 1
        for i in range(len(num1)):
            add_num = ""
            c = 0
            for j in range(len(num2)):
                c, p = self.multiply_1bit(num1[ind_end - i], num2[ind_end - j], c)
                add_num = p + add_num
            if c != 0:
                add_num = str(c) + add_num
            res = self.add(res, add_num + "0" * i)

        # 去掉前导的0
        res = res.lstrip("0")
        if res == "":
            res = "0"
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.multiply("9133", "0"))