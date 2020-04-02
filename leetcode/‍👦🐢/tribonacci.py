"""
泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        tbs = [0, 1, 1]
        i = 3
        while i < n + 1:
            tbs.append(tbs[i - 1] + tbs[i - 2] + tbs[i - 3])
            i += 1
        return tbs[-1]


if __name__ == '__main__':
    print(Solution().tribonacci(4))
    print(Solution().tribonacci(25))