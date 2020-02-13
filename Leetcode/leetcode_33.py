'''
搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

思路一：
先二分找到旋转点，然后将旋转后的下标映射回原来的下标，再进行标准二分查找，注意停止二分的边界检查
结果：40ms通过

思路二：
将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
结果：32ms通过
'''

class Solution(object):
    '''
    思路一
    '''
    # def log2phy(self, log_ind, offset, len_nums):
    #     '''
    #     逻辑下标映射到实际下标
    #     :param log_ind:
    #     :param offset:
    #     :param len_nums:
    #     :return:
    #     '''
    #     return (log_ind + offset) % len_nums
    #
    # def bi_search(self, nums, ind_start, ind_end, offset, target):
    #     if ind_start > ind_end: #
    #         return - 1
    #     log_ind = (ind_start + ind_end) // 2
    #     phy_ind = self.log2phy(log_ind, offset, len(nums))
    #     if nums[phy_ind] == target:
    #         return phy_ind
    #     elif nums[phy_ind] < target:
    #         return self.bi_search(nums, log_ind + 1, ind_end, offset, target)
    #     elif nums[phy_ind] > target:
    #         return self.bi_search(nums, ind_start, log_ind - 1, offset, target)
    #
    # def bi_search_offset(self, nums, ind_start, ind_end): #
    #     '''
    #     二分查找旋转点，返回旋转位移
    #     :param nums:
    #     :param ind_start:
    #     :param ind_end:
    #     :return:
    #     '''
    #     if ind_start > ind_end: #
    #         return 0
    #
    #     ind = (ind_start + ind_end) // 2
    #     if ind + 1 < len(nums) and nums[ind + 1] < nums[ind]: #
    #         return ind + 1 - 0
    #
    #     elif nums[ind] >= nums[0]:
    #         return self.bi_search_offset(nums, ind + 1, ind_end)
    #     elif nums[ind] < nums[0]:
    #         return self.bi_search_offset(nums, ind_start, ind - 1)
    #
    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     if len(nums) == 0:
    #         return -1
    #     offset = self.bi_search_offset(nums, 0, len(nums) - 1)
    #     return self.bi_search(nums, 0, len(nums) - 1, offset, target)

    '''
    思路二
    '''
    def bi_search(self, nums, ind_start, ind_end, target):
        '''
        二分查找
        :param nums:
        :param ind_start:
        :param ind_end:
        :param target:
        :return:
        '''
        if ind_start > ind_end:
            return -1
        ind_mid = (ind_start + ind_end) // 2
        if nums[ind_mid] == target:
            return ind_mid
        elif nums[ind_mid] > target:
            return self.bi_search(nums, ind_start, ind_mid - 1, target)
        else:
            return self.bi_search(nums, ind_mid + 1, ind_end, target)

    def search_(self, nums, ind_start, ind_end, target):
        '''
        增加ind_start和ind_end两个参数，方便递归调用
        :param nums:
        :param ind_start:
        :param ind_end:
        :param target:
        :return:
        '''
        if ind_start > ind_end:
            return -1
        ind_mid = (ind_start + ind_end) // 2
        if nums[ind_mid] >= nums[ind_start]:
            target_ind = self.bi_search(nums, ind_start, ind_mid, target)
            if target_ind == -1:
                return self.search_(nums, ind_mid + 1, ind_end, target)
            return target_ind
        else:
            target_ind = self.bi_search(nums, ind_mid + 1, ind_end, target)
            if target_ind == -1:
                return self.search_(nums, ind_start, ind_mid, target)
            return target_ind

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.search_(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([4,5,6,7,0,1,2], 3))
