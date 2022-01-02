from typing import List
from collections import deque

class Solution:
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     nums = sorted(nums)
    #     subsets = list()
    #     que = deque([[], ])
    #     while len(que):
    #         left = que.popleft()
    #         subsets.append(left)
    #         start_idx = 0 if len(left) == 0 else left[-1] + 1
    #         for i in range(start_idx, len(nums)):
    #             if i > start_idx and nums[i] == nums[i - 1]:
    #                 continue
    #             left_cp = left[:]
    #             left_cp.append(i)
    #             que.append(left_cp)
    #     return [[nums[idx] for idx in s] for s in subsets]

    # backtrace
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        subsets = list()
        def backtrace(bag, start_idx):
            subsets.append(bag[:])
            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i] == nums[i - 1]:
                    continue
                bag.append(nums[i])
                backtrace(bag, i + 1)
                bag.remove(nums[i])
        backtrace(list(), 0)
        return subsets


if __name__ == "__main__":
    s = Solution()
    print(s.subsetsWithDup([1, 2, 2]))