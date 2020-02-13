'''
Longest Substring Without Repeating Characters

idea:
sliding window
a|bcabca
    ^
'''

from collections import deque
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        解法一：set + queue
        '''
        # que = deque([])
        # bag = set()
        # max_len_substr = 0
        # for c in s:
        #     if c not in bag:
        #         bag.add(c)
        #         que.append(c)
        #     else:
        #         while True:
        #             c_pop = que.popleft()
        #             bag.remove(c_pop)
        #             if c_pop == c:
        #                 break
        #         que.append(c)
        #         bag.add(c)
        #     max_len_substr = max(max_len_substr, len(que))
        # return max_len_substr

        '''
        解法2: map
        每次循环都更新最大子串长度，遇到重复只做更新start的操作
        '''
        if len(s) == 0:
            return 0

        char2ind_dict = {s[0]: 0}
        start = 0
        max_len_substr = 1
        for i in range(1, len(s)):
            if s[i] in char2ind_dict:
                start = max(char2ind_dict[s[i]] + 1, start)# 遇到重复字符，更新start到子串重复字符之后，因为start之前的字符也还存在char2ind中，用max可以把小于start的忽略掉，不进行更新操作
            char2ind_dict[s[i]] = i
            max_len_substr = max(max_len_substr, i - start + 1)
        return max_len_substr


if __name__ == "__main__":
    solu = Solution()
    print(solu.lengthOfLongestSubstring("abba"))
