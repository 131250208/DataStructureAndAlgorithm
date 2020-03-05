# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        prepre = 1
        pre = 1
        if number == 0:
            return 1
        elif number == 1:
            return 1
        current = 0
        for i in range(2, number + 1):
            current = pre + prepre
            prepre = pre
            pre = current
        return current


if __name__ =="__main__":
    s = Solution()
    print(s.jumpFloor(3))