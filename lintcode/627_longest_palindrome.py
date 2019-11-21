"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.


Example 1:

Input : s = "abccccdd"
Output : 7
Explanation :
One longest palindrome that can be built is "dccaccd", whose length is `7`.

"""

__author__ = 'qingxi'


class MySolution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built

    思路：
    假设字符串里有n对相同字符，有m个单独的字符
    如果m=0，则返回2n
    如果m>0，则返回2n+1

    成绩：您的提交打败了 99.80% 的提交!
    """

    @staticmethod
    def longestPalindrome(s):
        # write your code here

        length = len(s)
        if length < 2:
            return length
        else:
            num = 0
            single = []
            for c in s:
                if c in single:
                    single.remove(c)
                    num += 2
                else:
                    single.append(c)
            if single:
                return num + 1
            else:
                return num


if __name__ == "__main__":
    assert MySolution.longestPalindrome("abccccdd") == 7
