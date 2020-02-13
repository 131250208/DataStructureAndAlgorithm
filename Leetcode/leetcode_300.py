'''
300. Longest Increasing Subsequence

思路1：二分搜索 + 贪心
思路2：动态规划
'''
class Solution:
    # def lengthOfLIS(self, nums) -> int:
    #     '''
    #     动态规划版
    #     :param nums:
    #     :return:
    #     '''
    #     dp = [1 for _ in range(len(nums))]
    #     max_len = 0
    #     for i in range(len(nums)):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[j] + 1, dp[i])
    #         max_len = max(max_len, dp[i])
    #     return max_len

    def upper_bound(self, dp, start, end, target):
        ind = (start + end) // 2
        while start < end:
            if target <= dp[ind]:
                end = ind #
            else:
                start = ind + 1
            ind = (start + end) // 2
        return ind

    def lengthOfLIS(self, nums) -> int:
        '''
        二分搜索 + 贪心
        :param nums:
        :return:
        '''
        dp = []
        for n in nums:
            if len(dp) == 0 or n > dp[-1]:
                dp.append(n)
            else:
                upper_ind = self.upper_bound(dp, 0, len(dp) - 1, n)
                dp[upper_ind] = n

        return len(dp)


if __name__ == "__main__":
    nums = [4,10,4,3,8,9]
    sol = Solution()
    print(sol.lengthOfLIS(nums))
