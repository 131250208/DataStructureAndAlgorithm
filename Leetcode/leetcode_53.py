'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

思路：
遍历每个数字，每次遍历都考虑一个问题：是否要重新开始一个序列？
如果这个数之前的序列起到的是负作用，则可以抛弃。

具体：
首先以第一个元素为一个子序列S1，判断其后的元素j 属不属于S1，应根据元素j 加上 S1的和后，是否比原来的值大。
若sum(S1,j) > sum(S1);则把j添加进S1，往后继续扫描。。
若sum(S1,j) < sum(S1);则j 为另一个（如S2）子序列的开始，以含一个S2的新子序列开始继续扫描。
最后返回和最大的子序列。
---------------------
作者：AceMa
来源：CSDN
原文：https://blog.csdn.net/acema/article/details/26979779
版权声明：本文为博主原创文章，转载请附上博文链接！
'''

class Solution:
    def maxSubArray(self, nums) -> int:
        if len(nums) == 0:
            return 0

        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            current_sum = current_sum + n if current_sum + n >= n else n
            max_sum = max(current_sum, max_sum)
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))