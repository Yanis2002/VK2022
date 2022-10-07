def main():
    game_field = [
        ['', '', ''],
        ['', '', ''],
        ['', '', '']
    ]
    game_on = True
    turn = True
    while game_on:
        flag = True
        turn = not turn
        for i in range(len(game_field)):
            for j in range(len(game_field[i])):
                print(f" {game_field[i][j]} |", end='')
            print('\n------------')
        while flag:
            inp = input(f"turn {'X' if turn else 'O'} pls write  'x y' ").split()
            flag = make_move(f"{'X' if turn else 'O'}", inp, game_field)
        game_on = not (check_winner(game_field) or check_draw(game_field))
    else:
        if check_draw(game_field):
            print("draw")
        else:
            print('X' if turn else "O", "winner")
        print("game over")


def check_winner(field):
    for i in range(len(field)):
        if field[0][i] == field[1][i] == field[2][i] != '' or field[i][0] == field[i][1] == field[i][2] != '':
            return True
    if field[0][0] == field[1][1] == field[2][2] != '' or field[0][2] == field[1][1] == field[2][0] != '':
        return True
    else:
        return False


def check_draw(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '':
                return False
    else:
        return True


def make_move(player, player_input, field):
    try:
        x, y = int(player_input[0]), int(player_input[1])
        if field[y][x] == '':
            field[y][x] = player
        else:
            print('already filled')
            return True
    except ValueError:
        print("not a number")
        return True
    except IndexError:
        print("incorrect input")
        return True
    else:
        return False


if __name__ == "__main__":
    main()
