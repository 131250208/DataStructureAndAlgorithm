'''
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''


class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda i: (i.start, i.end))

        pre = None
        intervals_new = []
        for ind, inter in enumerate(intervals):
            if ind == 0:
                pre = intervals[0]
                continue
            if inter.start <= pre.end:
                end = max(pre.end, inter.end)
                pre = Interval(pre.start, end)
            else:
                intervals_new.append(pre)
                pre = inter

        if pre:
            intervals_new.append(pre)

        return intervals_new


if __name__ == "__main__":
    intervals = [Interval(1, 4), Interval(0, 4)]
    sol = Solution()
    res = sol.merge(intervals)
    for i in res:
        print(i)
