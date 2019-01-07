class solution(object):
    def isMonotonic(self, A):
        incr = decr = True
        print(len(A))
        for iter in range(len(A) - 1):
            if A[iter] > A[iter + 1]:
                incr = False
            if A[iter] < A[iter + 1]:
                decr = False
        return incr or decr
            

obj = solution()
my_list = [5]
print(obj.isMonotonic(my_list))