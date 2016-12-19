# Using hash and one pass
class Solution(object):	
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i,v in enumerate(nums):
        	if target - v in d:
        		for val in d[target-v]:
        			if val!=i:
        				return(sorted([val,i]))

        	if v in d:
        		d[v].append(i)
        	else:
        		d[v] = [i]


#=================================================#

# Naive approach sorted+binsearch
class Solution(object):
    def binsearch(self, arr, key, src):
    	# Assume sorted input
		start = 0
		end = len(arr) - 1
		#loop
		while(start <= end):
			m = (start+end)/2
			if arr[m][1] == key:
				if arr[m][0] != src:
					return arr[m][0]
				else:
					return arr[m-1][0] if (m>0 and arr[m-1][1]==arr[m][1]) else arr[m+1][0]
			if arr[m][1] > key:
				end = m-1
			else:
				start = m+1
		return -1
	
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = [i for i in enumerate(nums)]
        arr = sorted(arr, key=lambda k:k[1])
        for i in arr:
        	res = self.binsearch(arr, target-i[1])
        	if res != -1:
        		return [i[0], res]

        
        