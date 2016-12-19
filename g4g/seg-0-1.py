
def segregate(arr):
	s = 0
	e = len(arr) - 1
	while(s < e):
		while(s < len(arr) and arr[s] == 0):
			s += 1
		while(e >= 0 and arr[e] == 1):
			e -= 1;
		if s < e:
			arr[s], arr[e] = arr[e],arr[s]
			s +=1
			e -=1
	return arr

if __name__ == '__main__':
	arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
	# arr = [0,0,0,0,0,0,0,0]
	# arr = [1,1,1,1,1,1,1]
	# arr = []
	# arr = [1,0,1,0,1]
	# arr = [0,1,0,0]
	print segregate(arr)


