'''
http://www.puzzles.ca/wordsearch/kids_cookies_solution.html

S I M A R C C E E T D N L T A
P A E A K O C U O N A E P E R
N U G A C A G M O P E C A N P
G U M O T N I M R E P P E P B
S I N P I A L C T S L U T O I
R U N R K A U U C H E N A A S
T S E G G I N G E O L O L T E
H M N N E A N O D R A A O M S
B U T T E R S C O T C H C E S
K U G P T N B A B B T S O A A
U S S S E U N R N R S M H L L
C I N N A M O N E E A C C A O
O M S N O O R A C A M N A S M
R A N I S I A R E D D U A R R

ALMOND
BRAN
BUTTERSCOTCH
CHOCOLATE
CINNAMON
COCONUT
GINGERBREAD
MACAROONS
MERINGUE
MOLASSES
OATMEAL
PEANUT
PECAN
PEPPERMINT
PUMPKIN
RAISIN
SHORTBREAD
SUGAR
'''

char_grid = [   "S I M A R C C E E T D N L T A",
                "P A E A K O C U O N A E P E R",
                "N U G A C A G M O P E C A N P",
                "G U M O T N I M R E P P E P B",
                "S I N P I A L C T S L U T O I",
                "R U N R K A U U C H E N A A S",
                "T S E G G I N G E O L O L T E",
                "H M N N E A N O D R A A O M S",
                "B U T T E R S C O T C H C E S",
                "K U G P T N B A B B T S O A A",
                "U S S S E U N R N R S M H L L",
                "C I N N A M O N E E A C C A O",
                "O M S N O O R A C A M N A S M",
                "R A N I S I A R E D D U A R R"]

words = [#"ALMOND",
#"BRAN",
#"BUTTERSCOTCH",
#"CHOCOLATE",
#"CINNAMON",
#"COCONUT",
#"GINGERBREAD",
#"MACAROONS",
#"MERINGUE",
#"MOLASSES",
#"OATMEAL",
#"PEANUT",
#"PECAN",
#"PEPPERMINT",
#"PUMPKIN",
"RAISIN",
#"SHORTBREAD",
#"SUGAR"
]

def search_nearby(i, j, di, dj, target, grid):
    cors = []
    if di == 0 and dj == 0:
        for x in xrange(i-1, i+2):
            for y in xrange(j-1, j+2):
                if not (x == i and y == j):
                    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if grid[x][y] == target:
                            cors.append((x,y,x-i,y-j))
    else:
        x = i + di
        y = j + dj
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            if grid[x][y] == target:
                cors.append((x,y,di,dj))
    return cors

def search_grid(char, grid):
    result = []
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == char:
                result.append((i,j))
    return result

def DFS(word, result, x, y, dx, dy, grid):
    target = word[0]
    cors = search_nearby(x, y, dx, dy, target, grid)
    print target, cors
    if cors:
        for i, j, di, dj in cors:
            if dx==dy==0 or (dx == di and dy == dj):
                result.append((i, j))
                if len(word) == 1:
                    print result, target, cors
                    return result
                else:
                    return DFS(word[1:], result, i, j, di, dj, grid)
    else:
        return []

t_grid = []
for chars in char_grid:
    char_list = chars.split(' ')
    t_grid.append(char_list)
char_grid = t_grid


result = []

for word in words:
    #print word
    first_cors = search_grid(word[0], char_grid)
    print first_cors
    for x,y in first_cors:
        word_cors = DFS(word[1:], [(x, y)], x, y, 0, 0, char_grid)
        print word_cors
        if len(word_cors) == len(word):
            result.append(word_cors)
            print word_cors
            break
print "****"
for x in result:
    print x
