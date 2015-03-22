def firstMissingPositive(A):
        for i in xrange(len(A)):
            while A[i] != i+1:
                if A[i] <= 0 or A[i] > len(A) or A[A[i]-1] == A[i]:
                    break
                else:
                    # i = 0
                    temp = A[i] # temp = A[0] = 2
                    A[i] = A[A[i]-1] # A[0] = A[1] = 1
                    print A[i]
                    A[A[i]-1] = temp # A[1] = temp = 2
                    print A[i], A[A[i]-1]
        for i in xrange(len(A)):
            if A[i] != i+1:
                return i+1
        return len(A)+1

print firstMissingPositive([2,1])
