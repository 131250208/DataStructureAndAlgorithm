'''
162. find peak element
'''
class Solution:
    def bisearch(self, nums, start, end):
        mid = (start + end) // 2
        if nums[mid - 1] < nums[mid] and nums[mid + 1] < nums[mid]:
            return mid
        elif nums[mid - 1] > nums[mid]:
            return self.bisearch(nums, start, mid - 1)
        else:
            return self.bisearch(nums, mid + 1, end)

    def findPeakElement(self, nums):
        nums += [float("-inf")]
        return self.bisearch(nums, 0, len(nums) - 1)
        pass

if __name__ == "__main__":
    nums = [1,2,1,3,5,6,4]
    sol = Solution()
    print(sol.findPeakElement(nums))
