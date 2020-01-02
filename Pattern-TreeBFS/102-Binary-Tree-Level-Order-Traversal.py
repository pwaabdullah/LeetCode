# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        queue, result = [], []
        if root is None: return result    # Edge condition
        queue.append(root)                # first node
        while queue:        
            levelResult = []                
            for _ in range(len(queue)):     # process level wise
                currentNode = queue.pop(0)
                levelResult.append(currentNode.val)
                if currentNode.left: queue.append(currentNode.left)         #push childs for next level
                if currentNode.right: queue.append(currentNode.right)
            result.append(levelResult)
        return result