"""
一个有名的按摩师会收到源源不断的预约请求，每个预约都可以选择接或不接。
在每次预约服务之间要有休息时间，因此她不能接受相邻的预约。
给定一个预约请求序列，替按摩师找到最优的预约集合（总预约时间最长），
返回总的分钟数。

示例 1：

输入： [1,2,3,1]
输出： 4
解释： 选择 1 号预约和 3 号预约，总时长 = 1 + 3 = 4。
示例 2：

输入： [2,7,9,3,1]
输出： 12
解释： 选择 1 号预约、 3 号预约和 5 号预约，总时长 = 2 + 9 + 1 = 12。
示例 3：

输入： [2,1,4,5,3,1,1,3]
输出： 12
解释： 选择 1 号预约、 3 号预约、 5 号预约和 8 号预约，总时长 = 2 + 4 + 3 + 3 = 12。
"""
from typing import *


class Solution:
    def massage(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) <= 2:
            return max(nums)
        result = [0 for i in range(len(nums))]
        result[0] = nums[0]
        result[1] = nums[1]
        for i in range(2, len(nums)):
            max_num = max(result[0:i - 1])
            result[i] = nums[i] + max_num
        return max(result)


# f(n) = n + max(f(n - 2), f(n -3), .. f(0))
if __name__ == '__main__':
    print(Solution().massage([2, 1, 4, 5, 3, 1, 1, 3]))
    print(Solution().massage([2, 7, 9, 3, 1]))
    print(Solution().massage([1,2,3,1]))
