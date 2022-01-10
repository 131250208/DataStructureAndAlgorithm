from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        parts = []
        def is_palindome(substr):
            i, n = 0, len(substr)
            j = n - 1 - i
            while i < j:
                if substr[i] != substr[j]:
                    return False
                i += 1
                j -= 1
            return True

        def backtrace(bag, s):
            if s == "":
                parts.append(bag[:])
            for idx in range(1, len(s) + 1):
                substr = s[:idx]
                if is_palindome(substr):
                    bag.append(substr)
                    backtrace(bag, s[idx:])
                    bag.pop()
        backtrace([], s)
        return parts

if __name__ == "__main__":
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("cbbbcc"))