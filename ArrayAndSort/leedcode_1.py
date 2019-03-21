'''
两数之和

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9
因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        考虑有多个答案的情况，虽然不是题目要求的，但是对三数之和有帮助
        用map映射num到index的list
        遍历每个数字，计算另一个加数，如果另一个加数已经存储在map中，
        遍历index的list返回所有结果
        '''
        # num2ind = {}
        # res_list = []
        # for ind, n in enumerate(nums):
        #     another_num = target - n
        #     if another_num in num2ind:
        #         for ind_ano in num2ind[another_num]:
        #             res_list.append([ind_ano, ind])
        #     if n in num2ind:
        #         num2ind[n].append(ind)
        #     else:
        #         num2ind[n] = [ind, ]
        # return res_list

        '''
        根据题目描述，只返回一个结果
        '''
        num2ind = {}
        for ind, n in enumerate(nums):
            another_num = target - n
            if another_num in num2ind:
                return [num2ind[another_num], ind]
            num2ind[n] = ind


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 2, 15], 9))