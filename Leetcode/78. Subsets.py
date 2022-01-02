from typing import List
from collections import deque

class Solution:
    # # backtrace
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     subsets = list()
    #     def backtrace(bag, start_idx):
    #         subsets.append(bag[:])
    #         for i in range(start_idx, len(nums)):
    #             bag.append(nums[i])
    #             backtrace(bag, i + 1)
    #             bag.remove(nums[i])
    #     backtrace(list(), 0)
    #     return subsets

    # iterate
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = list()
        que = deque([[], ])
        while len(que):
            left = que.popleft()
            subsets.append(left)
            start_idx = 0 if len(left) == 0 else left[-1] + 1
            for i in range(start_idx, len(nums)):
                left_cp = left[:]
                left_cp.append(i)
                que.append(left_cp)
        return [[nums[idx] for idx in s] for s in subsets]


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))