class Solution:
    # def GetUglyNumber_Solution(self, index):
    #     '''
    #     complexity of time is too large
    #     too much time
    #     :param index:
    #     :return:
    #     '''
    #     # write code here
    #     def isUglyNum(n, factors):
    #         for f in factors:
    #             while n % f == 0:
    #                 n /= f
    #         return n == 1
    #
    #     n = 0
    #     factors = [2, 3, 5]
    #     while index:
    #         n += 1
    #         if isUglyNum(n, factors):
    #             index -= 1
    #     return n

    def GetUglyNumber_Solution(self, index):
        '''
        short time, but need a list, complexity of space if O(index)
        :param index:
        :return:
        '''
        if index <= 0:
            return 0
        factors = [2, 3, 5]
        uglyNums = [1, ]
        factors_2_point = {f:0 for f in factors}

        index -= 1
        while index:
            uglyCandidates = [f * uglyNums[p] for f, p in factors_2_point.items()]
            uglyNums.append(min(uglyCandidates))
            for f, p in factors_2_point.items():
                while uglyNums[p] * f <= uglyNums[-1]:
                    p += 1
                factors_2_point[f] = p
            index -= 1
        return uglyNums[-1]

if __name__ == "__main__":
    s = Solution()
    print s.GetUglyNumber_Solution(14)