"""
#动态规划#
119. Edit Distance

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:

Input:
"horse"
"ros"
Output: 3
Explanation:
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')


Example 2:

Input:
"intention"
"execution"
Output: 5
Explanation:
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
"""


class MySolution:
    """
    @param word1: A string
    @param word2: A string
    @return: The minimum number of steps.

    思路：
    dp[i][j] 存储word1[0:i]与word2[0:j]的编辑次数，注意i=0 表示空字符串""，第1个字符从1开始

    case 1: word1[i]==word2[j]
    dp[i][j] = dp[i-1][j-1]

    case 2: word1[i]!=word2[j]
    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)

    成绩：您的提交打败了 46.80% 的提交!
    """

    def minDistance(self, word1, word2):
        # write your code here
        l1 = len(word1)
        l2 = len(word2)
        if l1 and l2:
            dp = [[0 for _ in range(l2 + 1)] for _ in range(l1 + 1)]

            for i in range(l1 + 1):
                for j in range(l2 + 1):
                    if i > 0 and j > 0:
                        if word1[i - 1] == word2[j - 1]:
                            dp[i][j] = dp[i - 1][j - 1]
                        else:
                            dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i - 1][j] + 1, dp[i][j - 1] + 1)
                    else:
                        dp[i][j] = max(i, j)

            return dp[l1][l2]
        else:
            return max(l1, l2)


if __name__ == "__main__":
    assert MySolution().minDistance("horse", "ros") == 3
    assert MySolution().minDistance("intention", "execution") == 5
