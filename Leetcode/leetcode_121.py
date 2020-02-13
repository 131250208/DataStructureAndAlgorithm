'''
买卖股票的最佳时机

最大收益 = max（过去i - 1天的最大收益，今天的收益）
今天的收益 = 今天的价格 - 历史最低价格
'''
class Solution:
    def maxProfit(self, prices) -> int:
        min_price = 99999999 # 过去 i - 1 天的最低价格
        max_income = 0 # 过去i - 1天可能的最大收益
        for p in prices:
            min_price = min(p, min_price)
            income_today = p - min_price
            max_income = max(income_today, max_income)
        return max_income

if __name__ == "__main__":
    prices = [7,6,4,3,1]
    sol = Solution()
    print(sol.maxProfit(prices))