from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combs = []
        def backtrace(bag, sum_, start_idx):
            # if sum_ > target:
            #     return
            if sum_ == target:
                combs.append(bag[:])
                return
            for i in range(start_idx, len(candidates)):
                if sum_ + candidates[i] > target:
                    continue
                bag.append(candidates[i])
                backtrace(bag, sum_ + candidates[i], i)
                bag.remove(candidates[i])
        backtrace([], 0, 0)
        return combs


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2, 3, 6, 7], 7))
    print(s.combinationSum([2, 3, 5], 8))