def switch(left, right, num, r):
    while right - left > 1:
        mid = (left+right)/2
        if r[mid] >= num:
            right = mid
        else:
            left = mid
    r[right] = num
    return

t = int(input())
r = []
r.append(int(raw_input().strip()))
sz = 1
for i in xrange(1, t):
    num = int(raw_input().strip())
    if num < r[0]:
        r[0] = num
    elif num > r[-1]:
        r.append(num)
        sz += 1
    else:
        switch(0, sz-1, num, r)
print sz
