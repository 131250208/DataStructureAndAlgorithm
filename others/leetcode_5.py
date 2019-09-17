'''
Manacher's Algorithm 计算最长回文子串
'''
import re
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = "#" + "#".join(s) + "#"
        pos, max_right = 0, 0
        RL = [1 for _ in range(len(s))]

        max_R, max_i = 1, 0
        for i in range(len(s)):
            if i < max_right:
                RL[i] = min(RL[2 * pos - i], max_right - i + 1)

            j = 1
            add_r = 0
            while i + RL[i] - 1 + j <= len(s) - 1 and i - (RL[i] - 1) - j >= 0 and s[i + RL[i] - 1 + j] == s[
                i - (RL[i] - 1) - j]:
                add_r += 1
                j += 1

            if add_r > 0:
                RL[i] += add_r

            if i + RL[i] - 1 > max_right:
                pos = i
                max_right = i + RL[i] - 1

            if RL[i] > max_R:
                max_R = RL[i]
                max_i = i

        return re.sub("#", "", s[max_i - max_R + 1:max_i + max_R - 1])

if __name__ == "__main__":
    sol = Solution()
    s = "cbbd"
    print(sol.longestPalindrome(s))
