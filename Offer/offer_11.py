class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 特例0：空数组
        if len(rotateArray) == 0:
            return 0
        left, right = 0, len(rotateArray) - 1
        # 特例1：完全有序
        if rotateArray[left] < rotateArray[right]:
            return rotateArray[0]
        while left < right:
            mid = (left + right) // 2

            # 特例2：三指针指向的数全等，无法判断，用顺序查找
            if rotateArray[left] == rotateArray[mid] and rotateArray[mid] == rotateArray[right]:
                pre = rotateArray[0]
                for i in range(1, len(rotateArray)):
                    if rotateArray[i] < pre:
                        return rotateArray[i]
                    pre = rotateArray[i]

            # 可判断旋转片段在哪一边
            if rotateArray[mid] > rotateArray[mid + 1]:
                return rotateArray[mid + 1]
            elif rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid


if __name__ == "__main__":
    s = Solution()
    print(s.minNumberInRotateArray([3, 4, 5, 1, 2]))