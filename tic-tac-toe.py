import os
import random
from time import sleep

def cls():
    os.system(['cls', 'clear'][os.name == 'posix'])

def player_type_input(n):
    player_type = ''
    while player_type not in ['C', 'H']:
        player_type = input(f'Player #{n}: Computer (C) or Human (H)? ').upper()
        if player_type not in ['C', 'H']:
            print('Wrong data enter')
    return player_type

def comp_lvl_input(n):
    lvl = ''
    while lvl not in ["0", "1", "2"]:
        lvl = input(f"Computer ({['0', 'X'][2 - n]}): Enter level (0-2) ")
        if lvl not in ["0", "1", "2"]:
            print('Wrong data enter')
    return lvl


def spot_input(player, field):
    spot = ''
    arr_field = list(field)
    while spot not in arr_field:
        spot = input(f"Player #{2 - player} ({['0', 'X'][player]}): Enter spot number ").upper()
        if spot not in arr_field:
            print('Wrong data enter')
    arr_field[arr_field.index(spot)] = ['0', 'X'][player]
    return ''.join(arr_field)

def check_simple_move(mark, field, lvl):
    moves = list('513792468')
    if lvl <= random.randint(0,1):
        random.shuffle(moves)
    for x in moves:
        if field[int(x)-1] == x:
            return x

def check_win_move(mark, field):
    win_combinations = [[(1,2),(4,8),(3,6)], [(0,2),(4,7)], [(0,1),(4,6),(5,8)],
                        [(0,6),(4,5)], [(0,8),(2,6),(3,5),(1,7)], [(2,8),(3,4)],
                        [(0,3),(2,4),(7,8)], [(1,4),(6,8)], [(2,5),(0,4),(6,7)]]
    for c, options in enumerate(win_combinations):
        if field[c] in 'X0':   continue
        for i1,i2 in options:
            if field[i1] == field[i2] == mark:
                return str(c+1)
    return -1

def spot_bot_input(player, field, lvl):
    spot = -1
    mark = ['0', 'X'][player]
    if lvl > random.randint(0, 1):
        spot = check_win_move(mark, field)
    if spot == -1 and lvl > random.randint(0,1):
        spot = check_win_move(['X', '0'][player], field)
    if spot == -1:
        spot = check_simple_move(mark, field, lvl)

    arr_field = list(field)
    arr_field[arr_field.index(spot)] = mark
    sleep(2)
    return ''.join(arr_field)


def draw_field(field):
    giant = {'1': ['...'.center(20)] * 6,
             '2': ['      .......       ',
                   '    ..       ..     ',
                   '           ...      ',
                   '         ...        ',
                   '      ...           ',
                   '    ...........     ', ],
             '3': ['      .......       ',
                   '    ..       ..     ',
                   '          ...      ',
                   '           ..        ',
                   '    ..       ..     ',
                   '      .......       ', ],
             '4': ['    ..       ..     ',
                   '    ..       ..     ',
                   '    ..       ..     ',
                   '    ...........     ',
                   '             ..     ',
                   '             ..     ', ],
             '5': ['    ...........     ',
                   '    ..              ',
                   '    .........       ',
                   '             ..     ',
                   '             ..     ',
                   '    ..........      ', ],
             '6': ['     .........      ',
                   '    ..              ',
                   '    .........       ',
                   '    ..       ..     ',
                   '    ..       ..     ',
                   '     .........      ', ],
             '7': ['    ...........     ',
                   '            ..      ',
                   '          ..        ',
                   '         ..         ',
                   '         ..         ',
                   '         ..         ', ],
             '8': ['       .....        ',
                   '     ..     ..      ',
                   '       .....        ',
                   '      ..   ..       ',
                   '    ..       ..     ',
                   '      .......       ', ],
             '9': ['     .........      ',
                   '    ..       ..     ',
                   '    ..       ..     ',
                   '     ..........     ',
                   '             ..     ',
                   '     .........      '],
             'X': ['    ██        ██    ',
                   '      ██    ██      ',
                   '        ████        ',
                   '        ████        ',
                   '      ██    ██      ',
                   '    ██        ██    '],
             '0': ['    ████████████    ',
                   '  ██            ██  ',
                   '  ██            ██  ',
                   '  ██            ██  ',
                   '  ██            ██  ',
                   '    ████████████    ']
             }
    vert = ' ' * 22 + '██' + ' ' * 24 + '██'
    horiz = '█' * 72
    cls()
    print(vert)
    for i in range(18):
        print(
            f"{giant[field[i // 6 * 3]][i % 6]}  ██  {giant[field[i // 6 * 3 + 1]][i % 6]}  ██  {giant[field[i // 6 * 3 + 2]][i % 6]}")
        if (i == 5 or i == 11): print(f"{vert}\n{horiz}\n{vert}")
    print(vert)
    # print(f"{field[0:3]}\n{field[3:6]}\n{field[6:]}")


def is_win(player, field):
    c = ['000', 'XXX'][player]
    lines = [field[:3], field[3:6], field[6:9], field[::3], field[1::3], field[2::3], field[::4], field[2:7:2]]
    return c in lines


def is_tie(field):
    return field.count('0') + field.count('X') == 9


field = '123456789'
player = True # True - 'X' (Player 1), False - '0' (Player 2)
cls()
print('Welcome to Tic-Tac-Toe!')
player_type = ['H', 'H']
bot = [0, 0]
for i in [0, 1]:
    player_type[i] = player_type_input(i + 1)
    if player_type[i] == 'C':
        bot[i] = int(comp_lvl_input(i + 1))

while not is_tie(field):
    cls()
    draw_field(field)
    if player_type[not player] == 'H':
        field = spot_input(player, field)
    else:
        field = spot_bot_input(player, field, bot[1-player])
    if is_win(player, field):
        draw_field(field)
        print(f'Player #{2 - player} won!')
        break
    player = not player

if is_tie(field):
    draw_field(field)
    print('The game is a tie!')
