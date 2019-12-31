# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root is None:
            return result
        
        queue = deque()
        queue.append(root)
        while queue:
            levelResult = []
            levelSize = len(queue)
            for _ in range(levelSize):
                currentNode  = queue.popleft()
                levelResult.append(currentNode.val)
                if currentNode.left:
                    queue.append(currentNode.left)
                if currentNode.right:
                    queue.append(currentNode.right)
                
            result.append(levelResult)
        return result