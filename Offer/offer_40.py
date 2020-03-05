# -*- coding:utf-8 -*-
class Solution:
    def _partition(self, nums, start, end, k):
        left, right = start, end
        flag = nums[left]
        while left < right:
            while left < right and nums[right] >= flag:
                right -= 1
            nums[left] = nums[right]
            while left < right and nums[left] <= flag:
                left += 1
            nums[right] = nums[left]
        nums[left] = flag
        if left < k - 1:
            self._partition(nums, left + 1, end, k)
        elif left > k - 1:
            self._partition(nums, start, left - 1, k)

    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k >= len(tinput) or not tinput or len(tinput) == 0:
            return tinput

        self._partition(tinput, 0, len(tinput) - 1, k)
        return tinput[:k]

if __name__ == "__main__":
    sol = Solution()
    nums, k = [4, 5, 1, 6, 2, 7, 3, 8], 4
    res = sol.GetLeastNumbers_Solution(nums, 4)
    print res