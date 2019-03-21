'''
结果：通过

字符串的排列

给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间

思路：
暴力解法是将s1的全排列全部算出来，再从s2找是否存在该排列。这样的解法第一步是O(n!)的复杂度，必定超时。

最好的解法是用滑动窗口，核心思想是：如果两个字符串的其中一个全排列相等，那么等价于他们的长度相等且字符频率相等。
所以，可以用两个长度为26的list来存储字符频率，第一个是目标串的频率记录，第二个是窗口的频率记录。
然后不断向后滑动窗口并与目标串的频率进行对比即可。
每次窗口的更新只需要调整窗口前的一个字符和新进入窗口的字符的频率。
'''


class Solution:
    def equal(self, list1, list2):
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
        return True

    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False

        target = [0 for i in range(26)]
        len_target = len(s1)
        window = [0 for i in range(26)]
        for c in s1:
            target[ord(c) - ord("a")] += 1

        for i in range(len_target):# 滑窗从头开始比较频率
            window[ord(s2[i]) - ord("a")] += 1

        if self.equal(window, target):
            return True

        point_start = 0
        for point_end in range(len_target, len(s2)):
            # 因为每次只移动一个字符，所以只需要进出字符的频率
            window[ord(s2[point_start]) - ord("a")] -= 1
            window[ord(s2[point_end]) - ord("a")] += 1
            if self.equal(window, target):
                return True
            point_start += 1
        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))