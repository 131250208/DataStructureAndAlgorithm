from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        win, res = deque([]), []
        for i, n in enumerate(nums):
            if win and win[0] <= i - k:
                win.popleft()
            while win and nums[win[-1]] < n:
                win.pop()
            win.append(i)
            if i >= k - 1:
                res.append(nums[win[0]])
        return res


if __name__ == "__main__":
    s = Solution()
    nums, k = [1, 3, 1, 2, 0, 5], 3
    res = s.maxSlidingWindow(nums, k)
    print(res)