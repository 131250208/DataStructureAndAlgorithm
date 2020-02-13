'''
接雨水

分别从左向右和从右向左画水平线
最后计算水量时，考虑两组水平线的最小值
因为水平线由两边较低的墙决定
'''


class Solution:
    def trap(self, height):
        left2right = [height[0] for _ in range(len(height))]
        right2left = [height[-1] for _ in range(len(height))]
        for ind, h in enumerate(height):
            if ind == 0:
                continue
            left2right[ind] = (max(left2right[ind - 1], h))
        for ind in range(len(height) - 1, -1, -1):
            if ind == len(height) - 1:
                continue
            right2left[ind] = (max(right2left[ind + 1], height[ind]))

        water = 0
        for ind in range(len(left2right)):
            level = min(left2right[ind], right2left[ind])
            water += level - height[ind]
        return water


if __name__ == "__main__":
    sol = Solution()
    print(sol.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
