# 题目 https://leetcode-cn.com/problems/merge-two-binary-trees/
# 日期：2019-11-02 周六 2:330~3:30

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTreesRecursion(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        递归
        :param t1:
        :param t2:
        :return:
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        t1.left = self.mergeTreesRecursion(t1.left, t2.left)
        t1.right = self.mergeTreesRecursion(t1.right, t2.right)
        return t1

    def mergeTreesIteration(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        迭代。。。不想写了
        :param t1:
        :param t2:
        :return:
        """

        pass


    @staticmethod
    def wrong(t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        死在了不知道怎么记录parent上。。。。。
        于是看答案去了。。。。

        思路：
            1. 首先，看到二叉树遍历问题，首先想到用list存储遍历过程处理的节点，处理过的节点pop移除，循环的终止条件是list为空。

            2. 接下来分析pop出来的节点可能出现的情况
            * 两个节点都不为空：两节点val值相加，赋值给节点1, 将子节点依次加入到队列中
            * 如果节点1为空，节点2不为空：节点1添加新节点，节点2赋值给节点1的parent
            * 如果节点1不为空，节点2为空：continue
            * 两个节点都为空：continue

            3. 需要记录parent
        """
        lst_parent1 = [None]
        lst_child1 = [t1]
        lst_child2 = [t2]
        while lst_child1 or lst_child2:
            parent = lst_parent1.pop()
            current1 = lst_child1.pop()
            current2 = lst_child2.pop()

            if current1 != None and current2 != None:
                current1.val += current2.val
                lst_parent1.append(current1.left)
                lst_child1.append(current1.left)
                lst_child2.append(current2.left)

                lst_parent1.append(current1.right)
                lst_child1.append(current1.right)
                lst_child2.append(current2.right)
            elif current1 == None and current2 != None:
                parent = current2
            else:
                continue

        return t1


if __name__ == '__main__':
    t1 = TreeNode(1)
    t1.left = TreeNode(3)
    t1.right = TreeNode(2)
    t1.left.left = TreeNode(5)

    t2 = TreeNode(2)
    t2.left = TreeNode(1)
    t2.right = TreeNode(3)
    t2.left.right = TreeNode(4)
    t2.right.right = TreeNode(7)

    t = Solution.mergeTrees(t1, t2)

    pass
