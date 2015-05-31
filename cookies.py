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

words = ["ALMOND",
"BRAN",
"BUTTERSCOTCH",
"CHOCOLATE",
"CINNAMON",
"COCONUT",
"GINGERBREAD",
"MACAROONS",
"MERINGUE",
"MOLASSES",
"OATMEAL",
"PEANUT",
"PECAN",
"PEPPERMINT",
"PUMPKIN",
"RAISIN",
"SHORTBREAD",
"SUGAR"]

def search_nearby(i, j, target, grid):

    for x in xrange(i, i+2):
        for y in xrange(j-1, j+2):
            if x >= 0 and x < len(grid) and \
                y >= 0 and y < len(grid[0]) and \
                x != i and y != j:
                if grid[x][y] == target:
                    print x, y
                    return [x, y]
    return False

def search_grid(char, grid):
    result = []
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == char:
                result.append([i,j])
    return result

t_grid = []
for chars in char_grid:
    char_list = chars.split(' ')
    t_grid.append(char_list)
char_grid = t_grid


result = []
for word in words:

    cors = search_grid(word[0], char_grid)
    temp = cors
    for c in xrange(len(cors)):
        for n in xrange(1, len(word)):
            cor = cors[c]
            i = cor[0]
            j = cor[1]
            pos = search_nearby(i, j, word[n], char_grid)
            if pos:
                temp[c].append(pos)
            else:
                break
    for t in temp:
        if len(t) == len(word):
            result.append(t)
print result
