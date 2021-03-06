"""
　　　　 ∧_∧::
　(⌒=- (Д｀ )::
⊂~ﾍ　 /⌒　 ⌒i/~つ
　＼＼/ ｜ 　| / /::
　　＼_/｜　 ヽ_/::
　　 　 /　　/::
　　　／　 　)::
　　／ ／/　/::
　 (　< /　/::
　　＼ (　ｲ_:
　　　`｜ | ):
　 　　｜ |/::
＿＿＿ /　)＿＿＿＿＿
　　　(_／

"""
#just make a test like a name of reverci

import sys
import random
import itertools
import functools
import operator

EMPTY = 0
BLACK = -1
WHITE = 1

#Goooooo
class S:
    def __init__(self, orig=None):
        self.board = []
        for i in range(8):
            self.board.append([EMPTY] * 8)

        self.board[3][3] = self.board[4][4] = BLACK
        self.board[4][3] = self.board[3][4] = WHITE
        
        if orig:
            assert isinstance(orig, S)
            for i in range(8):
                for j in range(8):
                    self.board[i][j] = orig.board[i][j]

#return n
    def count(self, bwe):
        assert bwe in (BLACK, WHITE, EMPTY)
        n = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == bwe:
                    n += 1
        return n

#my place 
    def itsmee(self, bw, x, y, delta_x, delta_y):
        assert bw in (BLACK, WHITE)
        assert delta_x in (-1, 0, 1)
        assert delta_y in (-1, 0, 1)
        x += delta_x
        y += delta_y

        if x < 0 or x > 7 or y < 0 or y > 7 or self.board[x][y] == EMPTY:
            return False
        if self.board[x][y] == bw:
            return True
        return self.itsmee(bw, x, y, delta_x, delta_y)

#got it 
    def supdirections(self, bw, x, y):
        assert bw in (BLACK, WHITE)

        directions = []
        if self.board[x][y] != EMPTY:
            return directions

        for d in itertools.product([-1,1,0],[-1,1,0]):
            if d == (0, 0):
                continue
            nx = x + d[0]
            ny = y + d[1]
            if nx < 0 or nx > 7 or ny < 0 or ny > 7 or self.board[nx][ny] != bw * -1:
                continue
            if self.itsmee(bw, nx, ny, d[0], d[1]):
                directions.append(d)
        return directions

#got it 
    def lol(self, bw, x, y, delta_x, delta_y):
        assert bw in (BLACK, WHITE)
        x += delta_x
        y += delta_y
        assert self.board[x][y] in (BLACK, WHITE)
#if it isnt snipet I should delete it 
        if self.board[x][y] == bw:
            return
        self.board[x][y] = bw
        return self.lol(bw, x, y, delta_x, delta_y)

#got it 
    def put(self, x, y, bw):
        assert bw in (BLACK, WHITE)
        directions = self.supdirections(bw, x, y)
        if len(directions) == 0:
            return False
        self.board[x][y] = bw
        for delta in directions:
            self.lol(bw, x, y, delta[0], delta[1])
        return True

#got it 
    def wazzap(self, bw, weight_matrix):
        assert bw in (BLACK, WHITE)
        my_score = 0
        against_score = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == bw:
                    my_score += weight_matrix[i][j]
                elif self.board[i][j] == bw * -1:
                    against_score += weight_matrix[i][j]
        return my_score - against_score

#got it
    def thebestass(self, bw, weight_matrix):
        assert bw in (BLACK, WHITE)

        next_positions = {}
        for i in range(8):
            for j in range(8):
                reversi = S(self)
                if reversi.put(i, j, bw):
                    next_positions.setdefault(
                        reversi.wazzap(bw, weight_matrix), []
                    ).append((i, j))
        if next_positions:
            next_position = random.choice(next_positions[max(next_positions)])
        else:
            next_position = None
        return next_position

#-------------------------------------------------------------------------------#

map1 = [
    [120, -20, 20, 5, 5, 20, -20, 120],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [20, -5, 15, 3, 3, 15, -5, 20],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [5, -5, 3, 3, 3, 3, -5, 5],
    [20, -5, 15, 3, 3, 15, -5, 20],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [120, -20, 20, 5, 5, 20, -20, 120],
]

#I should change like a delete one under map or + - .

map2 = [
    [30, -12, 0, -1, -1, 0, -12, 30],
    [-12, -15, -3, -3, -3, -3, -15, -12],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [-1, -3, -1, -1, -1, -1, -3, -1],
    [0, -3, 0, -1, -1, 0, -3, 0],
    [-12, -15, -3, -3, -3, -3, -15, -12],
    [30, -12, 0, -1, -1, 0, -12, 30],
]
#can change as now 

#-------------------------------------------------------------------------------#

BLACK_MARK = 'M' #me
WHITE_MARK = 'S' #cp

#making board image on terminal
def printontheboard(reversi):
    print('\n   a b c d e f g h \n  *-*-*-*-*-*-*-*-*')  #\n = (LF）
    for i, row in enumerate(reversi.board):
        print(' %d|' % (i+1), end='')
        for r in row:
            print('{}|'.format({EMPTY: ' ', BLACK: BLACK_MARK, WHITE: WHITE_MARK}[r]), end='')
        print('\n  *-*-*-*-*-*-*-*-*')                   #\n = (LF）
    print()

#start~
def intolevel():
    while True:
        s = input('Hows it going dude! Plz push "ENTER"')
        if s == '':
            return 1
        if s in ('enter'):
            return int(s)

#like a me
def topoftheposition(player):
    while True:
        s = input('{}? [a~h][1~8]'.format(BLACK_MARK if player == BLACK else WHITE_MARK))
        if s == 'enter' or (len(s) == 2 and s[0] in list('abcdefgh') and s[1] in list('12345678')):
            break
    if s == '':
        return None
#upper is into 'enter'. its mean like a if i push enter or typo, it have to return.

    y, x = ord(s[0]) - 97, ord(s[1]) - 49
    return x, y

#skip
def putpositionontheterminal(player, xy):
    if xy is None:
        print('{}: skip'.format(BLACK_MARK if player == BLACK else WHITE_MARK))
    else:
        print('{}: {}{}'.format(
            BLACK_MARK if player == BLACK else WHITE_MARK,
            chr(xy[1]+97),
            chr(xy[0]+49),
        ))

    if player is None:
        print('{}: skip') 

#maybe its a misunderstand but I'll try that

#done
#I have to make future like...I mean something like that


#starrrrrt
def yoyowassapdude():
    reversi = S()
    level = intolevel()
    if level == '':
        weight_matrix = map1
    else:
        weight_matrix = map2

    player = BLACK
    while not (
        reversi.count(EMPTY) == 0 or
        reversi.count(BLACK) == 0 or
        reversi.count(WHITE) == 0
    ):
        printontheboard(reversi)
        xy = topoftheposition(player)
        while xy and not reversi.put(xy[0], xy[1], player):
            xy = topoftheposition(player)

        printontheboard(reversi)
        xy = reversi.thebestass(player * -1, weight_matrix)
        if xy:
            reversi.put(xy[0], xy[1], player * -1)
        putpositionontheterminal(player * -1, xy)

    printontheboard(reversi)
    if reversi.count(player) > reversi.count(player * -1):
        print('You win!')
    elif reversi.count(player) < reversi.count(player * -1):
        print('You lose!')

#doneee
if __name__ == "__main__":
    yoyowassapdude()
    
#__main__ & __name__ is like a only  "Python3" hah  
#finaly I gatta make python3 + ML or DL in mmy knowledge maybe after harf year 
#-------------------------------------------------------------------------------#