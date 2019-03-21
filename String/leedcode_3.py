'''
Longest Substring Without Repeating Characters

idea:
sliding window
a|bcabca
    ^
'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        解法一，用了string.index()函数，这个函数是找子串的，本身有性能消耗。不过时间已经足够短了。
        '''
        # max_len_substr = 0
        # substr = ""
        # for c in s: # 遍历目标字符串
        #     if c in substr: # 如果已经存在于子串中，更新一次最大长度，并截掉子串中包括重复字符及之前的部分
        #         if len(substr) > max_len_substr:
        #             max_len_substr = len(substr)
        #         substr = substr[substr.index(c) + 1:]
        #     substr += c # 无论有无重复字符，都将新字符加入到当前子串的末尾
        #
        # # 遍历结束再做一次更新，避免目标串中没有重复字符导致没有进行最大长度更新（因之前的更新操作是遇到重复字符才进行的
        # if len(substr) > max_len_substr:
        #     max_len_substr = len(substr)
        # return max_len_substr

        '''
        解法2: c++ 风格
        每次循环都更新最大子串长度，遇到重复只做更新start的操作
        '''
        char2ind = {}
        start, max_len_substr = 0, 0
        for ind, c in enumerate(s):
            if c in char2ind:
                start = max(char2ind[c] + 1, start) # 遇到重复字符，更新start到子串重复字符之后，因为start之前的字符也还存在char2ind中，用max可以把小于start的忽略掉

            char2ind[c] = ind # 字符到索引的映射
            current_len = ind - start + 1 # 当前子串长度
            if current_len > max_len_substr: # 更新最大长度的操作
                max_len_substr = current_len

        return max_len_substr


if __name__ == "__main__":
    solu = Solution()
    print(solu.lengthOfLongestSubstring(" "))