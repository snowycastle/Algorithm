"""
667 Longest Palindromic Subsequence

Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000

"""

__author__ = 'qingxi'


class MySolution:
    @staticmethod
    def longestPalindromeSubseq(s):
        """
        思路：
        用dp[i][j] 记录字符串从i到j的最大回文长度

        步骤：
        1. 初始化dp[i][j] 为单位矩阵
        2. 长度为2时，如果相邻字符相同，则dp[i][i+1]为2
        3. 长度大于2时，dp[i][j] 为 max(dp[i+1][j],dp[i][j-1], dp[i+1][j-1]+2 且s[i]==s[j])

        成绩：您的提交打败了 45.40% 的提交!
        """
        # write your code here
        length = len(s)

        if length <= 1:
            return length

        else:
            dp = [[1 for _ in range(length)] for _ in range(length)]

            for i in range(length - 1):
                j = i + 1
                if s[i] == s[j]:
                    dp[i][j] = 2

            for step in range(2, length):
                for i in range(length - step):
                    j = i + step
                    if s[i] == s[j]:
                        dp[i][j] = dp[i + 1][j - 1] + 2
                    else:
                        dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

            return max([max(row) for row in dp])


class OtherSolution:
    @staticmethod
    def longestPalindromeSubseq(s):
        """
        这个逻辑更清晰

        思路：
        用dp[i][j] 记录字符串从i到j的最大回文长度

        case1: s[i] != s[j]
        sub(i,j)的最大回文要么出现在sub(i+1,j)，要么出现在sub(i,j-1)


        case2: s[i]==s[j]
        sub(i,j)的最大回文等于sub(i+1,j-1)的最大回+2

        注意计算sub(i,j)需要事先已计算sub(i+1,j-1)，因此i要从大到小遍历，j要从小到大遍历

        只用一个循环

        成绩：您的提交打败了 35.00% 的提交!
        """
        length = len(s)

        if length <= 1:
            return length

        else:
            dp = [[0 for _ in range(length)] for _ in range(length)]

            for i in range(length - 1, -1, -1):
                dp[i][i] = 1
                if i + 1 < length:
                    for j in range(i + 1, length):
                        if s[i] == s[j]:
                            dp[i][j] = dp[i + 1][j - 1] + 2
                        else:
                            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
            return dp[0][length - 1]


if __name__ == "__main__":
    assert MySolution.longestPalindromeSubseq(
        "abcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcba") == 73

    assert OtherSolution.longestPalindromeSubseq(
        "abcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcbabcdefgfedcba") == 73
