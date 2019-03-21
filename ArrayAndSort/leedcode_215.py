'''
数组中的第K个最大元素
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

思路：
建立最大堆，出堆K次
'''

class Solution(object):
    def swap(self, nums, i1, i2):
        '''
        swap num1 and num2
        :param nums:
        :param i1: index of num1
        :param i2: index of num2
        :return:
        '''
        temp = nums[i1]
        nums[i1] = nums[i2]
        nums[i2] = temp

    def siftdown(self, nums, i):
        '''
        do sift down
        :param nums:
        :param i:
        :return:
        '''
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        greater_child = -1

        if left_child < len(nums): # check if left child index is out of range
            greater_child = left_child
            # check if right child index is in the range and greater than left child
            if right_child < len(nums) and nums[right_child] > nums[left_child]:
                greater_child = right_child

        if 0 < greater_child < len(nums) and nums[greater_child] > nums[i]:
            self.swap(nums, i, greater_child)
            self.siftdown(nums, greater_child)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # build a maximum heap
        last_parent = (len(nums) - 2) // 2
        for i in range(last_parent, -1, -1):
            self.siftdown(nums, i)

        # pop K times to find the Kth max num
        res = 0
        for i in range(k):
            res = nums[0]
            last = nums.pop()
            if len(nums) == 0:
                break
            nums[0] = last
            self.siftdown(nums, 0)
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.findKthLargest([1], 1))
