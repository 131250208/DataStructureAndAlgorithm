from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        combs = []
        def backtrace(bag, sum_, start_idx):
            if sum_ == target:
                combs.append(bag[:])
            for i in range(start_idx, len(candidates)):
                if sum_ + candidates[i] > target or i > start_idx and candidates[i] == candidates[i - 1]:  # pruning
                    continue
                bag.append(candidates[i])
                backtrace(bag, sum_ + candidates[i], i + 1)
                bag.remove(candidates[i])
        backtrace([], 0, 0)
        return combs


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(s.combinationSum2([2, 5, 2, 1, 2], 5))