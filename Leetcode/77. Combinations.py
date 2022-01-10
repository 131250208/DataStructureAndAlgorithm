from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combs = []
        def backtrace(bag, start_idx):
            if len(bag) + (n - 1 - start_idx) + 1 < k:
                return  # pruning 2
            if len(bag) == k:
                combs.append(bag[:])
                return  # pruning 1
            for i in range(start_idx, n):
                bag.append(i + 1)
                backtrace(bag, i + 1)
                bag.remove(i + 1)
        backtrace([], 0)
        return combs

if __name__ == "__main__":
    s = Solution()
    print(s.combine(4, 2))