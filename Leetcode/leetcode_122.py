'''
买卖股票的最佳时机 II
'''

class Solution:
    def maxProfit(self, prices) -> int:
        pre_price = 999999
        income = 0
        for p in prices:
            pre_price = min(p, pre_price)
            if p - pre_price > 0:
                income += p - pre_price
                pre_price = p
        return income


if __name__ == "__main__":
    prices = [1,2,3,4,5]
    sol = Solution()
    print(sol.maxProfit(prices))