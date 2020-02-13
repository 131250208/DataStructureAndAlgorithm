'''
结果：通过
题目：
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
思路：以第一个字符串为标准，依次对比每一个字符。
'''
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        str1 = strs[0]
        point = 0
        count_common = 0
        while True:
            hit_all = True
            for str in strs:
                if len(str) == 0 or point >= len(str) or point >= len(str1):
                    hit_all = False
                    break
                if str[point] != str1[point]:
                    hit_all = False
            if hit_all:
                count_common += 1
            else:
                break
            point += 1
        return str1[:count_common]


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonPrefix(["dog","racecar","car"]))