"""
1. Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""
class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        if not word:
            return True
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.check(board, word, i, j):
                    return True
        return False

    def check(self, board, word, i, j):
        if board[i][j] == word[0]:
            # If iterated all chars in word
            if not word[1:]:
                return True
            # Mark board[i][j] as used
            board[i][j] = " "
            if i > 0 and self.check(board, word[1:], i-1, j):
                return True
            elif i + 1 < len(board) and self.check(board, word[1:], i+1, j):
                return True
            elif j > 0 and self.check(board, word[1:], i, j-1):
                return True
            elif j + 1 < len(board[0]) and self.check(board, word[1:], i, j+1):
                return True
            # change it back
            board[i][j] = word[0]
            return False
        else:
            return False

"""
2.Rotate image.
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""
class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.

    # Naive solution, create a new matrix
    def rotate(self, matrix):
        n = len(matrix)
        newm = [[0 for x in range(n)] for y in range(n)]
        for i in xrange(n):
            for j in xrange(n):
                newm[j][n-1-i] = matrix[i][j]

        matrix = newm

    # In-place, loop by loop
    # new_j = i
    def rotate(self, matrix):
        n = len(matrix)
        length = n
        for i in xrange(n/2):
            m = length - 1
            for j in xrange(m):
                temp =                  matrix[i][i+j]
                matrix[i][i+j] =        matrix[i+m-j][i]
                matrix[i+m-j][i] =      matrix[i+m][i+m-j]
                matrix[i+m][i+m-j] =    matrix[i+j][i+m]
                matrix[i+j][i+m] =      temp

            length -= 2

    """
    First swap based on diagnal, and then swap based on midline:
    1 2 ->  1 3 ->  3 1
    3 4     2 4     4 2
    """
    def rotate(self, matrix):
        n = len(matrix)
        for i in xrange(n):
            for j in xrange(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(n):
            for j in xrange(n/2):
                matrix[i][j], matrix[i][n-j-1] =  matrix[i][n-j-1], matrix[i][j]

