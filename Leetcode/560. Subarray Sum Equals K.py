from typing import List
from collections import deque
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_ = 0
        sum2count = {0: 1}
        count = 0
        for n in nums:
            sum_ += n
            if sum_ - k in sum2count:
                count += sum2count[sum_ - k]
            sum2count[sum_] = sum2count.get(sum_, 0) + 1
        return count


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1, 2, 3], 3))
    print(s.subarraySum([-1, -1, 1], 0))