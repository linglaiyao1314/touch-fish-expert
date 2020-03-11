"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

"""
from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_value = 0
        if len(prices) < 2:
            return 0
        i, j = 0, 1
        while j < len(prices):
            if prices[i] > prices[j]:
                i += 1
            else:
                value = prices[j] - prices[i]
                if max_value < value:
                    max_value = value
                j += 1
        return max_value


if __name__ == '__main__':
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(Solution().maxProfit([1, 2, 1, 3, 7]))
