'''
167.
'''
class Solution:
    def twoSum(self, numbers, target):
        ## 用map的方法
        # map = {}
        # for ind, n in enumerate(numbers):
        #     t = (target - n)
        #     if t in map:
        #         return [map[target - n] + 1, ind + 1]
        #     map[n] = ind

        ## 用双指针
        start, end = 0, len(numbers) - 1
        while numbers[start] + numbers[end] != target:
            if numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1

        return [start + 1, end + 1]

if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(numbers, target))
