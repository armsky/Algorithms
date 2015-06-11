# Generates the next permutation lexicographically after a given permutation.
# It changes the given permutation in-place.
def nextPermutation(s):
    # s is a array(list in python)
    """
    Find the highest index i such that s[i] < s[i+1].
    If no such index exists, the permutation is the last permutation.
    """
    for i in reversed(xrange(len(s))):
        if s[i] > s[i-1]:
            break
    else:
        return []
    i -= 1
    """
    Find the highest index j > i such that s[j] > s[i].
    Such a j must exist, since at least i+1 is such an index.
    """
    for j in reversed(xrange(i+1, len(s))):
        if s[j] > s[i]:
            break
    """
    swap s[i] with s[j]
    """
    s[i], s[j] = s[j], s[i]
    """
    Reverse all the order of all of the elements after index i
    """
    s[i+1 :] = reversed(s[i+1 : ])
    # s[i+1:].sort()
    return s
