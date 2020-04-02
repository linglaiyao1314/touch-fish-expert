class Solution:
    def mySqrt(self, x: int) -> int:
        """
        (a/2) ** 2 <= a
        """
        left = 0
        right = x // 2 + 1
        while left < right:
            mid = (left + right + 1) // 2
            square = mid * mid
            if square > x:
                right = mid - 1
            else:
                left = mid
        return left


if __name__ == '__main__':
    print(Solution().mySqrt(10))