
from bst import *
class Solution:
    def range_sum_bst1_test(self):
        val = [10, 5, 15, 3, 7, 18]
        t = Tree()
        for i in val:
            t.insert(i)
        print(self.range_sum_bst1(t.root, 7, 15))

    def range_sum_bst1(self, root: TreeNode, L: int, R: int) -> int:
        sum = 0
        if root is None:
            return 0
        if root.val >= L and root.val <= R:
            sum += root.val
        if root.val > L:
            sum += self.range_sum_bst1(root.left, L, R)
        if root.val < R:
            sum += self.range_sum_bst1(root.right, L, R)
        return sum

    def max_height_test(self):
        val = [10, 5, 15, 3, 7, 18]
        t = Tree()
        for i in val:
            t.insert(i)
        print(self.max_height(t.root))

    def max_height(self, root: TreeNode):
        if not root:
            return 0
        return 1 + max(self.max_height(root.left), self.max_height(root.right))

    def numTrees(self, n: int) -> int:
        

if __name__ == '__main__':
    sol = Solution()
    sol.range_sum_bst1_test()
    sol.max_height_test()
