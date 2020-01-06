"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
示例 1:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
输出: true
示例 2:

输入:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
输出: false
"""
from typing import *


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        left, right = 0, rows * cols
        while left < right:
            mid = (left + right) // 2
            row = mid // cols
            col = mid % cols
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                right = mid
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    print(Solution().searchMatrix(matrix=[
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ],
        target=20))
