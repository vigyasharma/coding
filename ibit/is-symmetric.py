import copy
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    # 0=false=not symetric, 1=true=symmetric
    def isSymmetric(self, A):
    	return self.isSymmetricImpl(A, A)
    	

    # Returns mirror image of tree provided
    def getMirror(self, node):
    	if not node:
    		return None

        t = TreeNode(node.val)
        t.left = self.getMirror(node.right)
        t.right = self.getMirror(node.left)
    	return t


    # Check if two trees are equal
    def isEqual(self, A, B):
    	if not A and not B:
    		return True

    	if not A or not B:
    		return False

    	return A.val == B.val and self.isEqual(A.left, B.left) and self.isEqual(A.right, B.right)


    # Check if two trees are symmetrical
    def isSymmetricImpl(self, A, B):
    	if not A and not B:
    		return True

    	if not A or not B:
    		return False

    	return A.val == B.val and self.isSymmetricImpl(A.left, B.right) and self.isSymmetricImpl(A.right, B.left)








