# Maximum Depth of a Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

#  Input: root = [3,9,20,null,null,15,7]
# Output: 3
# Example 2:

# Input: root = [1,null,2]
# Output: 2
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            leftDepth=self.maxDepth(root.left)
            rightDepth=self.maxDepth(root.right)
        return 1+max(leftDepth,rightDepth)
    
     # level=0
        # q=deque([root])
        # while q:

        #     for i in range(len(q)):
        #         node=q.popleft()
        #         if node.left:
        #            q.append(node.left)
        #         elif node.right:
        #             q.append(node.right)
        #     level+=1
        # return level# return 1+max(leftDepth,rightDepth)

    

        #iterative DSf
        stack=[[root,1]]
        res=0
        while stack:
            node,depth=stack.pop()
            if node:
                res=max(res,depth)
                stack.append([node.left,depth+1])
                stack.append([node.right,depth+1])
        return res
            
    

    
    
    