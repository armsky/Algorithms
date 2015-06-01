def titleToNumber(s):
    n = len(s)
    b = 1
    result = 0
    for i in xrange(len(s)-1, -1, -1):
        if b-1 == 0:
            result += ord(s[i]) - 64
        else:
            result +=  26**(b-1) * (ord(s[i]) - 64)
        b += 1

        if b > n:
            return result
print titleToNumber('ZAA')
