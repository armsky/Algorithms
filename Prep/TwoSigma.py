"""
1.Fibonacci coding
Give a positive integer, use Fibonacci codingreturn a string
i.e. give 4 will return "101"
"""
def fi_encoding(n):
    if n < 1:
        return ""
    fi = [1,2]
    while fi[-1] < n:
        fi.append(fi[-1] + fi[-2])
    if fi[-1] > n:
        fi = fi[:-1]
    print fi
    re = ""
    for i in range(len(fi)-1, -1, -1):
        if fi[i] <= n:
            re = '1'+re
            n -= fi[i]
        else:
            re = '0'+re

    return re

"""
2. Longest Chain
Give a list of words. remove one char in a word, if the modified word still in the list, the length of chain plus 1. Find the longest chain length.
"""
def longest_chain2(words):
    if not words:
        return 0
    ws = set(words)
    cur_len = 0
    max_len = 0
    for word in ws:
        max_len = find2(word, ws, cur_len+1, max_len)
    return max_len

def find2(word, ws, cur_len, max_len):
    if cur_len > max_len:
        max_len = cur_len
    for i in range(len(word)):
        new_word = word[:i]+word[i+1:]
        if new_word in ws:
            max_len = find2(new_word, ws, cur_len+1, max_len)
    return max_len

def longest_chain(words):
    if not words:
        return 0
    word_dic = {}
    max_len = 0
    cur_len = 0
    for word in words:
        if word not in word_dic:
            word_dic[word] = 1
    for word in words:
        max_len = find(word, word_dic, cur_len+1, max_len)
    return max_len

def find(word, word_dic, cur_len, max_len):
    if cur_len > max_len:
        max_len = cur_len
    for i in range(len(word)):
        new_word = word[:i]+word[i+1:]
        if new_word in word_dic:
            max_len = find(new_word, word_dic, cur_len +1, max_len)
    return max_len

"""
3. Friend Circle
Give a string of friends
    ynyy
    nyyn
    yyyn
    ynny

Find how many circles among those people.
"""

def friend_circle(friends):
    n = len(friends)
    import Queue
    q = Queue.Queue()
    visited = [False] * n
    circle = 0
    for i in range(n):
        if visited[i] == False:
            q.put(i)
            visited[i] = True
            while q.qsize() > 0:
                f = q.get()
                for j in range(n):
                    if visited[j] == False and friends[f][j] == 'Y':
                        visited[j] = True
                        q.put(j)
            circle += 1
    return circle

friends = [
        "YYNN",
        "YYYN",
        "NYYN",
        "NNNY"]

#print friend_circle(friends)


words = ["a","abcd","bcd","abd","cd","c", "abcde"]
print  longest_chain(words)
print longest_chain2(words)


#print fi_encoding(1)
#print fi_encoding(2)
#print fi_encoding(9)
#print fi_encoding(65)
