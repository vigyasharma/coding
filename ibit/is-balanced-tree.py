# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
    	is_height_balanced = self.isBalancedImpl(A)[0]
    	return 1 if is_height_balanced else 0

    def isBalancedImpl(self, node):
    	if not node:
    		return (True, 0)

    	lbal, lheight = self.isBalancedImpl(node.left)
    	if not lbal:
    		return (lbal, lheight+1)
    	rbal, rheight = self.isBalancedImpl(node.right)
    	if not rbal:
    		return (rbal, rheight+1)

    	return ( abs(lheight - rheight) <= 1, max(lheight, rheight) + 1 )
