class Solution:
    # @param A : tuple of integers
    # @return an integer
    # Sum should contain at least one number from the array
    def maxSubArray(self, A):
    	maxSum = A[0]
    	currSum = 0
    	for i in range(1, len(A)):
    		currSum += A[i]
    		maxSum = max(maxSum, currSum)
    		currSum = max(currSum, 0)
    	return maxSum
