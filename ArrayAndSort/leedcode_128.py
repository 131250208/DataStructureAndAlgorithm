'''
128. 最长连续序列

给定一个未排序的整数数组，找出最长连续序列的长度。
要求算法的时间复杂度为 O(n)。

示例:
输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。

思路：
用哈希表存储每个端点值对应连续区间的长度
若数已在哈希表中：跳过不做处理
若是新数加入：
    取出其左右相邻数已有的连续区间长度 left 和 right
    计算当前数的区间长度为：cur_length = left + right + 1
    根据 cur_length 更新最大长度 max_length 的值
    更新区间两端点的长度值 # 重要步骤，因为之后的数字更新区域长度，只会访问到已存在连续区域的端点
'''

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_exist = {}
        max_len = 0
        for n in nums:
            if n not in num_exist:
                continuous_len = 0
                left_len = num_exist.get(n - 1, 0) # 取 n - 1，如果没有，返回默认的0
                right_len = num_exist.get(n + 1, 0)
                continuous_len += left_len
                continuous_len += right_len
                continuous_len += 1

                num_exist[n] = continuous_len
                num_exist[n - left_len] = continuous_len
                num_exist[n + right_len] = continuous_len

                if continuous_len > max_len:
                    max_len = continuous_len

        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))