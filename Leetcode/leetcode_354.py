import numpy as np
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        envelopes = sorted(envelopes, key=lambda x: (x[0], -x[1])) # 为什么第二维要倒着排？
        return self.lengthOfLIS(envelopes)

    def upper_bound(self, dp, start, end, target):
        ind = (start + end) // 2
        while start < end:
            if target[1] > dp[ind][1]:
                start = ind + 1
            else:
                end = ind #
            ind = (start + end) // 2

        return ind

    def greater_than(self, env1, env2):
        return env1[0] > env2[0] and env1[1] > env2[1]

    def lengthOfLIS(self, envs) -> int:
        '''
        二分搜索 + 贪心
        :param envs:
        :return:
        '''
        dp = []
        for e in envs:
            if len(dp) == 0 or self.greater_than(e, dp[-1]):
                dp.append(e)
            else:
                upper_ind = self.upper_bound(dp, 0, len(dp) - 1, e)
                # if upper_ind != -1:
                dp[upper_ind] = e

        return len(dp)


if __name__ == "__main__":
    env = [[30,50],[12,2],[3,4],[12,15]]
    sol = Solution()
    print(sol.maxEnvelopes(env))
