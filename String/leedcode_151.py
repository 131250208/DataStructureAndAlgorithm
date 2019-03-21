'''
翻转字符串里的单词

给定一个字符串，逐个翻转字符串中的每个单词。

示例:

输入: "the sky is blue",
输出: "blue is sky the".
说明:

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
进阶: 请选用C语言的用户尝试使用 O(1) 空间复杂度的原地解法。

思路：
以空格切割字符串，用栈缓存words再弹栈输出

'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(" ")
        stack = []
        for w in words:
            if w != "":
                stack.append(w)

        res = []
        while len(stack):
            res.append(stack.pop())

        return " ".join(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))