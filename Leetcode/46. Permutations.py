from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        def backtrace(bag):
            if len(bag) == len(nums):
                permutations.append(bag[:])
            for n in nums:
                if n not in bag:
                    bag.append(n)
                    backtrace(bag)
                    bag.remove(n)
        backtrace([])
        return permutations


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))