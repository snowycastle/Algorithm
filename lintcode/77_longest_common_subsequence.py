"""
77. Longest Common Subsequence

Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

样例
Example 1:
	Input:  "ABCD" and "EDCA"
	Output:  1

	Explanation:
	LCS is 'A' or  'D' or 'C'


Example 2:
	Input: "ABCD" and "EACB"
	Output:  2

	Explanation:
	LCS is "AC"

What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm

#动态规划#
"""


class MySolution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    成绩：您的提交打败了 100.00% 的提交!
    """

    def longestCommonSubsequence(self, A, B):
        """
        思路：动态规划 不用说了
        :param A:
        :param B:
        :return:
        """
        # write your code here
        len_a = len(A)
        len_b = len(B)
        if len_a == 0 or len_b == 0:
            return 0
        dp = [[0 for _ in range(len_b + 1)] for _ in range(len_a + 1)]
        for i in range(len_a + 1):
            for j in range(len_b + 1):
                if i == 0 or j == 0:
                    continue
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
                else:
                    dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        return dp[len_a][len_b]


if __name__ == '__main__':
    assert MySolution().longestCommonSubsequence("ABCD", "EACB") == 2
    assert MySolution().longestCommonSubsequence("ABCD", "EDCA") == 1
