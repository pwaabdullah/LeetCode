# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        queue, result = [], []
        if root is None: return result
        queue.append(root)
        direction = True
        while queue:
            levelResult = deque()
            for _ in range(len(queue)):
                currentNode  = queue.pop(0)
                # append level results
                if direction: levelResult.append(currentNode.val)
                else: levelResult.appendleft(currentNode.val)
                # append childs to the Q for next level
                if currentNode.left: queue.append(currentNode.left)
                if currentNode.right: queue.append(currentNode.right)

            result.append(levelResult)
            # changing direction at every level
            if direction: direction = False
            else: direction=True
                
        return result