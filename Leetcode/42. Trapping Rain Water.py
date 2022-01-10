from typing import List

class Solution:
    def trap(self,  height: List[int]) -> int:
        water_level = height[:]
        max_pre = -1
        for i in range(len(height)):
            max_pre = max(max_pre, height[i])
            water_level[i] = max_pre

        max_pre = -1
        for i in range(len(height) - 1, -1, -1):
            max_pre = max(max_pre, height[i])
            water_level[i] = min(max_pre, water_level[i])

        water = 0
        for i in range(len(height)):
            water += water_level[i] - height[i]
        return water


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))