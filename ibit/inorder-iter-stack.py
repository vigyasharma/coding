# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
    	inorder = []
    	stack = []
    	curr = A
    	while (curr or stack):
    		if curr:
    			while curr.left:
    				stack.append(curr)
    				curr = curr.left
    		else:
    			curr = stack.pop()
    		inorder.append(curr.val)
    		curr = curr.right

    	return inorder
