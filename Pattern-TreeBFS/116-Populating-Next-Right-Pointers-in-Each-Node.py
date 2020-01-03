"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        queue, result = [], []
        if root is None: return root    # Edge condition
        queue.append(root)
        
        while queue:
            currentNode = queue.pop(0)
            if currentNode.left and currentNode.right:      
                currentNode.left.next = currentNode.right   # Condition 1
            
                if currentNode.next:
                    currentNode.right.next = currentNode.next.left  # Condition 2
            
                queue.append(currentNode.left)
                queue.append(currentNode.right)
        return root