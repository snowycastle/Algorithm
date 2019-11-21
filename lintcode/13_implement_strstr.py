"""
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Example 1:

Input: source = "source" ，target = "target"
Output: -1
Explanation: If the source does not contain the target content, return - 1.
Example 2:

Input:source = "abcdabcdefg" ，target = "bcd"
Output: 1
Explanation: If the source contains the target content, return the location where the target first appeared in the source.

挑战
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)

"""


class MySolution:
    """
    @param source:
    @param target:
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        t_len = len(target)
        s_len = len(source)
        if s_len==0 and t_len==0:
            return 0
        elif s_len>0 and t_len==0:
            return 0
        elif t_len > s_len:
            return -1
        else:
            for i in range(s_len):
                if source[i:i+t_len]==target:
                    return i
                else:
                    continue
            return -1


if __name__ == '__main__':
    assert MySolution().strStr("a", "") == 0
    assert MySolution().strStr("","") == 0
    assert MySolution().strStr("","a") == -1
    assert MySolution().strStr("source", "target") == -1
    assert MySolution().strStr("abcde", "e") == 4


