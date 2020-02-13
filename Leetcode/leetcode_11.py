class Solution:
    def maxArea(self, height) -> int:
        max_area = 0
        line_left, line_right = 0, len(height) - 1
        while line_left < line_right:
            current_area = min(height[line_left], height[line_right]) * (line_right - line_left)
            max_area = max(max_area, current_area)

            if height[line_left] < height[line_right]:
                line_left += 1
            else:
                line_right -= 1

        return max_area

if __name__ == "__main__":
    sol = Solution()
    height = [2,3,4,5,18,17,6]
    print(sol.maxArea(height))
