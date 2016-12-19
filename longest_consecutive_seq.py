# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Example: 
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

# Your algorithm should run in O(n) complexity.
##########################################

from collections import defaultdict
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
    	h = { i:True for i in A }
        maxlen = 0
        for i in A:
            num = i
            c = 0
            if i in h:
                c = 1
                del(h[i])
            else:
                continue
            num = i + 1
            while num in h:
                c += 1
                del(h[num])
                num += 1
            num = i - 1
            while num in h:
                c += 1
                del(h[num])
                num -= 1
            maxlen = max(maxlen, c)
        return maxlen
            