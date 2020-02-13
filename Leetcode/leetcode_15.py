'''
 三数之和

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。
注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
from itertools import combinations

class Solution(object):
    def twoSum(self, nums, start_ind, target):
        '''
        两数之和，O(N)
        :param nums:
        :param target:
        :return:
        '''
        num_exi = set() # 储存被使用过的加数，用于去重
        another_num_set = set() # 储存出现过的加数，以备使用
        for ind in range(start_ind, len(nums)):
            n = nums[ind]
            another_num = target - n
            if n in num_exi:
                continue
            if another_num in another_num_set:
                yield another_num, n
                num_exi.add(n)
            another_num_set.add(n)

        # -------------------------------------------------
        pass

    def threeSum(self, nums):
        """
        基于两数之和，O(N*N)
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # res_list = []
        # nums.sort() # 很重要，去重
        # num_exi = set()
        # for ind, n in enumerate(nums):
        #     if n not in num_exi:
        #         target_4_two_sum = 0 - n
        #         for num1, num2 in self.twoSum(nums, ind + 1, target_4_two_sum):
        #             res_list.append([n, num1, num2])
        #     num_exi.add(n)
        # return res_list

        # ---------------------------------------------------
        return self.n_sum(nums, 3, 0)

    def n_sum(self, nums, n, target):
        if n == 2:
            exi_set = set()
            ban_set = set()
            res_list = []
            for num in nums:
                if num in ban_set:
                    continue
                addent = target - num
                if addent in exi_set:
                    res_list.append([addent, num])
                    ban_set.add(num)
                    ban_set.add(addent)
                exi_set.add(num)
            return res_list
        else:
            res_list = []
            exi_set = set()
            # nums = sorted(nums)
            for i in range(len(nums)):
                if nums[i] in exi_set:
                    continue
                res_list_pre = self.n_sum(nums[i + 1:], n - 1, target - nums[i])

                for res_pre in res_list_pre:
                    res_pre.append(nums[i])
                    res_list.append(res_pre)
                exi_set.add(nums[i])
            return res_list

    def fourSum(self, nums, target):
        return self.n_sum(nums, 4, target)
if __name__ == "__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(sol.threeSum(nums))
