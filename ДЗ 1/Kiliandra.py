def move():
    field, moves, players, game, turn = [['', '', ''], ['', '', ''], ['', '', '']], [[0, 0], [0, 1], [0, 2], [1, 1], [1, 2], [2, 2]], ['O', 'X'], None, 0
    while game == None:
        print(' 0 1 2\n0', field[0], '\n1', field[1], '\n2', field[2], '\n')
        try:
            x, y = input(players[turn] + "'s move: ").split(',')
            x, y = int(x), int(y)
            if ([x, y] in moves or [y, x] in moves) and field[x][y] == '':
                field[x][y] = players[turn]
                turn = abs(turn-1)
                if draw_check(field, game) != None: game = draw_check(field, game)
                elif win_check(field, game) != None: game = win_check(field, game)
            else: print('\ninvalid move')
        except: print('\ninput error')
    else: print(' 0 1 2\n0', field[0], '\n1', field[1], '\n2', field[2], '\n', '\n', players[abs(turn-1)], game)

def draw_check(field, game):
    if '' not in field[0] and '' not in field[1] and '' not in field[2]: return 'draw'

def win_check(field, game):
    for k in range(3):
        if (field[k][0] == field[k][1] == field[k][2] != '' or field[0][k] == field[1][k] == field[2][k] != '') or (
        field[0][0] == field[1][1] == field[2][2] != '' or field[0][2] == field[1][1] == field[2][0] != ''): return 'win'

move()