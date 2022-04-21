cpdef int test(int x):
	cdef int y=0
	cdef ibt i
	for i in range(x):
		y+=i
	return y
