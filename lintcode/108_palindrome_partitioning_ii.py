"""
108. Palindrome Partitioning II

Given a string s, cut s into some substrings such that every substring is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

样例
Example 1:

Input: "a"
Output: 0
Explanation: "a" is already a palindrome, no need to split.
Example 2:

Input: "aab"
Output: 1
Explanation: Split "aab" once, into "aa" and "b", both palindrome.
"""


class Solution:
    """
    @param s: A string
    @return: An integer

    总结：

    动态规划总的思路是从上一个状态推断当前状态。
    处理细节上要注意的点：
    1. 要注意第1个状态的处理，要么增加一个初始状态值，要么跳过第1个状态
    2. 要注意合理的遍历顺序和范围

    这道题首先构建出二维数组isPalindrome，isPalindrome[i][j]表示是下标从i到下标为j之间构成的字符串是否是回文串。
    定义数组表示前i个字母，最少切割几次可以切割为都是回文串。i从1开始到s.length()，然后j从1开始到i结束。
    如果isPalindrome[j][i]是回文串，即s[j]-s[i]之间是回文串，则最少只需要1次切割(对半切割)即可分成两个回文串，
    则前i个字母所需要的最小切割次数为f[i]和前j个字母所需最小切割次数f[j-1]+1之间的较小值。所以f[i]=min(f[i],f[j]+1).

    成绩：您的提交打败了 54.00% 的提交!
    """

    def minCut(self, s):
        # write your code here
        palin = self.isPalindorm(s)

        # 如果s[0][i]是回文则初始化dp[i]=0, 否则初始化为s[0~i]的最大分割数即i
        dp = [0 if palin[0][i] else i for i in range(len(s))]

        for i in range(1, len(s)):
            for j in range(1, i + 1):
                if i < len(s) and palin[j][i]:
                    dp[i] = min(dp[j - 1] + 1, dp[i])

        return dp[len(s) - 1]

    def isPalindorm(self, s):
        l = len(s)
        dp = [[0 for _ in range(l)] for _ in range(l)]
        for mid in range(l):
            i = j = mid
            while i >= 0 and j <= l - 1 and s[i] == s[j]:
                dp[i][j] = True
                i -= 1
                j += 1
            i = mid
            j = mid + 1
            while i >= 0 and j < l and s[i] == s[j]:
                dp[i][j] = True
                i -= 1
                j += 1

        return dp


if __name__ == '__main__':
    s = Solution()
    assert s.minCut('a') == 0
    assert s.minCut('aa') == 0
    assert s.minCut('aab') == 1
    assert s.minCut('aabcac') == 2
