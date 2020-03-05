def my_quick_sort(nums, start, end):
    if start >= end:
        return

    left, right = start, end
    flag = nums[left]
    while left < right:
        while left < right and nums[right] >= flag:
            right -= 1
        nums[left] = nums[right]
        while left < right and nums[left] <= flag:
            left += 1
        nums[right] = nums[left]

    nums[left] = flag
    my_quick_sort(nums, start, left - 1)
    my_quick_sort(nums, left + 1, end)



