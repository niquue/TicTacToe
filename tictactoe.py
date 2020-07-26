# write your code here
# str_list = input("Enter cells: > ")
# user_prompt = user_prompt.split(" ")
str_list = list()
for i in range(9):
    str_list.append(' ')
# print(str_list)


def print_board():
    print("---------")
    print("| " + str_list[0] + " " + str_list[1] + " " + str_list[2] + " |")
    print("| " + str_list[3] + " " + str_list[4] + " " + str_list[5] + " |")
    print("| " + str_list[6] + " " + str_list[7] + " " + str_list[8] + " |")
    print("---------")



print_board()


def diagonal(x):
    if str_list[0] == x and str_list[4] == x and str_list[8] == x:
        return True
    elif str_list[2] == x and str_list[4] == x and str_list[6] == x:
        return True
    else:
        return False


def horizontal(x):
    if str_list[0] == x and str_list[1] == x and str_list[2] == x:
        return True
    elif str_list[3] == x and str_list[4] == x and str_list[5] == x:
        return True
    elif str_list[6] == x and str_list[7] == x and str_list[8] == x:
        return True
    else:
        return False


def vertical(x):
    if str_list[0] == x and str_list[3] == x and str_list[6] == x:
        return True
    elif str_list[1] == x and str_list[4] == x and str_list[7] == x:
        return True
    elif str_list[2] == x and str_list[5] == x and str_list[8] == x:
        return True
    else:
        return False


# check_x = 'X'
# check_o = 'O'

def check_x():
    _x = 'X'
    if diagonal(_x):
        return True
    elif horizontal(_x):
        return True
    elif vertical(_x):
        return True
    else:
        return False


def check_o():
    _o = 'O'
    if diagonal(_o):
        return True
    elif horizontal(_o):
        return True
    elif vertical(_o):
        return True
    else:
        return False


def check_impossible():
    num_x = 0
    num_o = 0

    for i in range(len(str_list)):
        if str_list[i] == 'X':
            num_x += 1
        elif str_list[i] == 'O':
            num_o += 1

    if check_x() and check_o():
        return True
    elif (num_x - num_o >= 2) or (num_o - num_x >= 2):
        return True
    else:
        return False


def check_not_finished():
    num_empty = 0
    for i in range(len(str_list)):
        if str_list[i] == '_' or str_list[i] == ' ':
            num_empty += 1
    if not check_o() and not check_x() and not check_impossible() and num_empty >= 1:
        return True
    else:
        return False


def check_board(x, y):
    board = str_list
    if x == '1':
        if y == '1':
            board = str_list[6]
        elif y == '2':
            board = str_list[3]
        elif y == '3':
            board = str_list[0]
    elif x == '2':
        if y == '1':
            board = str_list[7]
        elif y == '2':
            board = str_list[4]
        elif y == '3':
            board = str_list[1]
    elif x == '3':
        if y == '1':
            board = str_list[8]
        elif y == '2':
            board = str_list[5]
        elif y == '3':
            board = str_list[2]

    if board == 'X' or board == 'O':
        return False
    else:
        return True


def place_board(x, coord_one, coord_two):
    # new_board = user_prompt
    if coord_one == '1':
        if coord_two == '1':
            str_list[6] = x
        elif coord_two == '2':
            str_list[3] = x
        elif coord_two == '3':
            str_list[0] = x
    elif coord_one == '2':
        if coord_two == '1':
            str_list[7] = x
        elif coord_two == '2':
            str_list[4] = x
        elif coord_two == '3':
            str_list[1] = x
    elif coord_one == '3':
        if coord_two == '1':
            str_list[8] = x
        elif coord_two == '2':
            str_list[5] = x
        elif coord_two == '3':
            str_list[2] = x


def check_board_full():
    count_empty = 0
    for i in range(len(str_list)):
        if str_list[i] == ' ':
            count_empty += 1
    if count_empty == 0:
        return True
    else:
        return False


def game_win():

    if check_x() and not check_o():
        print("X wins")
        return True
    elif check_o() and not check_x():
        print("O wins")
        return True
    # elif check_impossible():
        # print("Impossible")
        # return True
    # elif check_not_finished():
        # print("Game not finished")
        # return True
    # elif not check_x() and not check_o():
        # print("Draw")
        # return True
    else:
        return False


coord_in = input("Enter the coordinates: > ").split()
# for i in range(len(coord_in)):
#    coord_in[i] = int(coord_in[i])

# print(coord_in)
user_start = 'X'
while True:
    if not coord_in[0].isdigit() or not coord_in[1].isdigit():
        print("You should enter numbers!")
        coord_in = input("Enter the coordinates: > ").split()
    elif int(coord_in[0]) > 3 or int(coord_in[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        coord_in = input("Enter the coordinates: > ").split()
    elif not check_board(coord_in[0], coord_in[1]):
        print("This cell is occupied! Choose another one!")
        coord_in = input("Enter the coordinates: > ").split()
    elif not game_win():
        place_board(user_start, coord_in[0], coord_in[1])
        print_board()
        if game_win():
            # print_board()
            break
        elif check_board_full():
            print("Draw")
            break
        if user_start == 'X':
            user_start = 'O'
        else:
            user_start = 'X'
        # print_board()
        coord_in = input("Enter the coordinates: > ").split()


# place_board('X', coord_in[0], coord_in[1])
# print_board()


