# -*- coding:utf-8 -*-
class Solution:
    def _myCmp(self, num1Str, num2Str):
        combineStr1 = num1Str + num2Str
        combineStr2 = num2Str + num1Str
        if combineStr1 < combineStr2:
            return -1
        elif combineStr1 > combineStr2:
            return 1
        return 0

    def PrintMinNumber(self, numbers):
        # write code here

        numbersStrList = [str(n) for n in numbers]
        numbersStrList.sort(cmp=self._myCmp)
        return "".join(numbersStrList)

if __name__ == "__main__":
    s = Solution()
    nums = [2, 3, 1, 5, 4]
    print s.PrintMinNumber(nums)