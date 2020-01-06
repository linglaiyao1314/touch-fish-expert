"""
假设你正在给爷爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。

你有多少种不同的方法可以爬到楼顶呢？
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        f[i] = f[i - 1] + f[i - 2]
        """
        if n < 1:
            return 0
        num_array = [0, 1, 2]
        stairs = 3
        while stairs <= n:
            num_array.append(num_array[stairs - 2] + num_array[stairs - 1])
            stairs += 1
        return num_array[n]


if __name__ == '__main__':
    print(Solution().climbStairs(9))
