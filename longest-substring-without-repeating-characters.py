? abcdsechfis

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        h = {}
        maxlen = 0
        currlen = 0
        start = 0
        for i in s:
        	if i not in h:
        		h[i] = True
        		currlen += 1
        	else:
        		while(s[start] != i):
        			del h[s[start]]
        			start += 1
        			currlen -= 1
        		del h[s[start]]
        		start += 1
        		h[i] = True
    		maxlen = max(maxlen, currlen)
    	return maxlen

