"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""

from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        min_pos = self.find_rotate_pos(nums)
        res = self.binary_search(nums, min_pos, len(nums), target)
        if res >= 0:
            return res
        return self.binary_search(nums, 0, min_pos, target)

    def binary_search(self, nums, start, end, target):
        while start < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid + 1
        return -1

    def find_rotate_pos(self, nums):
        """寻找"""
        if nums[0] < nums[-1]:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if nums[pivot] > nums[pivot + 1]:
                return pivot + 1
            else:
                if nums[pivot] < nums[left]:
                    right = pivot - 1
                else:
                    left = pivot + 1
        return 0


if __name__ == '__main__':
    # print(Solution().search([1, 2, 3, 4, 5], 1))
    # print(Solution().search([2, 3, 4, 5, 1], 2))
    print(Solution().find_rotate_pos([2, 3, 4, 5, 1]))
