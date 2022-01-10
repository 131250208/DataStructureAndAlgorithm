from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = []
        def backtrace(bag, sum_, start_num):
            if len(bag) > k or sum_ > n:
                return  # pruning 2
            if len(bag) == k and sum_ == n:
                combs.append(bag[:])
                return  # pruning 1
            for i in range(start_num, 10):
                bag.append(i)
                backtrace(bag, sum_ + i, i + 1)
                bag.remove(i)
        backtrace([], 0, 1)
        return combs


if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum3(3, 7))
    print(s.combinationSum3(3, 9))