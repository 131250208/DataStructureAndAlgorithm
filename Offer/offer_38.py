# -*- coding:utf-8 -*-
class Solution:
    def _Permutation(self, ss):
        if ss == "":
            return ["", ]

        perListTotal = []
        for i in range(len(ss)):
            subStr = ss[:i] + ss[i+1:]
            perList = self._Permutation(subStr)
            for p in perList:
                perListTotal.append(ss[i] + p)
        return list(set(perListTotal))

    def Permutation(self, ss):
        for p in sorted(self._Permutation(ss)):
            print p

if __name__ == "__main__":
    ss = ""
    s = Solution()
    s.Permutation(ss)