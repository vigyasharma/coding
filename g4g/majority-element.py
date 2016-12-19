
def binfirst(arr, key):
	l = 0
	h = len(arr) - 1
	while(l<=h):
		print "\n"
		m = (l+h)/2
		print l,m,h
		print arr[l],arr[m],arr[h]
		if arr[m] == key and (m == 0 or arr[m-1] < arr[m]):
			return m
		if key > arr[m]:
			l = m+1
		else:
			h = m-1

if __name__ == '__main__':
	# arr = [1, 2, 3, 3, 3, 3, 10]
	# arr = [1, 1, 4, 4, 4, 4, 6, 6]
	arr = [1,2,2]
	n = len(arr)
	key = arr[n/2]
	first = binfirst(arr, key)
	count = n/2 + 1 # quorum condition
	if (first + count - 1) < n and arr[first+count-1] == key:
		print "Majority element is %d" % key
	else:
		print "No majority element present"
