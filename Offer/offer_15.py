class Solution:
    def NumberOf1(self, n):
        count = 0
        while n != 0:
            n = n & (n - 1)
            count += 1
        return count

        # count = 0
        # flag = 1
        # max_flag = 0x100000000
        # while flag != max_flag:
        #     if n & flag:
        #         count += 1
        #     flag = flag << 1
        # return count

if __name__ == "__main__":
    s = Solution()
    print(s.NumberOf1(0xFCFF))