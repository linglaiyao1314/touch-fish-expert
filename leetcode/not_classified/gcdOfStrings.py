"""
对于字符串 S 和 T，只有在 S = T + ... + T（T 与自身连接 1 次或多次）时，我们才认定 “T 能除尽 S”。

返回最长字符串 X，要求满足 X 能除尽 str1 且 X 能除尽 str2。

 

示例 1：

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"
示例 2：

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"
示例 3：

输入：str1 = "LEET", str2 = "CODE"
输出：""

"""


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) <= 0 or len(str2) <= 0:
            return ""
        if str1[0] != str2[0]:
            return ""
        s = str1 + str2
        gcd_str = str2 if len(str1) >= len(str2) else str1
        max_gcd_size = len(gcd_str)
        while gcd_str != "":
            gcd_size = len(gcd_str)
            start = 0
            end = gcd_size
            while start < len(s):
                if s[start:end] == gcd_str:
                    start, end = end, end + gcd_size
                else:
                    break
            if start == len(s) and max_gcd_size % len(gcd_str) == 0:
                return gcd_str
            gcd_size -= 1
            gcd_str = gcd_str[:gcd_size]
        return gcd_str


if __name__ == '__main__':
    print(Solution().gcdOfStrings(str1="TAUXXTAUXXTAUXXTAUXXTAUXX",
                                  str2="TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
    print(Solution().gcdOfStrings(str1="ABC",
                                  str2="ABCABC"))
