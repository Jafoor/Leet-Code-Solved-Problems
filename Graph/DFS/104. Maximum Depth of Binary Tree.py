#RECURSIVE APPROACH

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        
        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))




#Using STACK
class Solution:
    def maxDepth(self, root):     
         if not root:
             return 0

         tstack,h = [root],0

         #count number of levels
         while tstack:
             nextlevel = []
             while tstack:
                 top = tstack.pop()
                 if top.left:
                     nextlevel.append(top.left)
                 if top.right:
                     nextlevel.append(top.right)
             tstack = nextlevel
             h+=1
         return h

#Using DEQUE

class Solution:
    def maxDepth(self, root):     
         if not root:
             return 0

         tqueue,h = collections.deque(),0
            
         tqueue.append(root)
        
         while tqueue:
            nextlevel = collections.deque()
            
            while tqueue:
                front = tqueue.popleft()
                if front.left:
                    nextlevel.append(front.left)
                if front.right:
                    nextlevel.append(front.right)
            h += 1
            tqueue = nextlevel
         return h

















