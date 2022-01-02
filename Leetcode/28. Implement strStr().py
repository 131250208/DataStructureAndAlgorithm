class Solution:
    # KMP
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        # get next
        next_ = [-1, ]
        i, j = 0, -1
        while i != len(needle):
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                next_.append(j)
            else:
                j = next_[j]

        # get index
        i, j = 0, 0
        while j < len(needle) and i < len(haystack):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next_[j]

        if j == len(needle):
            return i - len(needle)
        else:
            return -1

    # # built-in function
    # def strStr(self, haystack: str, needle: str) -> int:
    #     try:
    #         idx = haystack.index(needle)
    #     except Exception as e:
    #         idx = -1
    #     return idx


if __name__ == "__main__":
    s = Solution()
    print(s.strStr("hello", "ll"))