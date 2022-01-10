from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        subs = []

        def backtrace(bag, start_idx):
            if len(bag) >= 2:
                subs.append(bag[:])
            mem = set()  # do not use the same num on the same level
            for i in range(start_idx, len(nums)):
                if nums[i] in mem:
                    continue
                mem.add(nums[i])
                if len(bag) == 0 or nums[i] >= bag[-1]:
                    bag.append(nums[i])
                    backtrace(bag, i + 1)
                    bag.pop()
        backtrace([], 0)
        return subs

if __name__ == "__main__":
    s = Solution()
    for sample in [[4, 6, 7, 7], [4, 4, 3, 2, 1]]:
        print(s.findSubsequences(sample))