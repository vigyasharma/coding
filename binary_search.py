

def binsearch(arr, key):
	arr = sorted(arr)
	start = 0
	end = len(arr) - 1
	#loop
	while(start <= end):
		m = (start+end)/2
		if arr[m] == key:
			return m
		if arr[m] > key:
			end = m-1
		else:
			start = m+1
	raise Exception("Key %d not found in %s" % (key, arr))

def main():
	arr = [1,2,4,5,7,8,10]


