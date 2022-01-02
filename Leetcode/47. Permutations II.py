from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        permutations = []
        def backtrace(bag):
            if len(bag) == len(nums):
                permutations.append(bag[:])

            pre = None
            for i in range(len(nums)):
                if i != 0 and nums[i] == pre:
                    continue
                if i not in bag:
                    bag.append(i)
                    pre = nums[i]
                    backtrace(bag)
                    bag.remove(i)
        backtrace([])
        return [[nums[idx] for idx in p_ids] for p_ids in permutations]


if __name__ == "__main__":
    s = Solution()
    print(s.permuteUnique([1, 2, 3]))
    print(s.permuteUnique([1, 1, 2]))