# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.pathSumRecursive(root, sum, [], result)
        return result

    def pathSumRecursive(self, root, sum, levelResult, result):
        if root is None: return         

        levelResult.append(root.val)

        if root.val == sum and root.left is None and root.right is None: result.append(list(levelResult))
        else: 
            self.pathSumRecursive(root.left, sum-root.val, levelResult, result)
            self.pathSumRecursive(root.right, sum-root.val, levelResult, result)

        del levelResult[-1]