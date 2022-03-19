result = list(range(9))
used = []

def inp_player_1():
    valid = True
    while valid:
        inp = int()
        try: inp = int(input("Ход 1-ого игрока! Выберите номер ячейки для Х ___"))
        except:
            print("Убедитесь, что Вы ввели целое число")
            continue
        if  inp in used:
            print("Эта ячейка уже занята. Выберите другую ячейку")
        else:
            result[inp] = "Х"
            used.append(inp)
            valid = False

def inp_player_2():
    valid = True
    while valid:
        inp = int()
        try: inp = int(input("Ход 2-ого игрока! Выберите номер ячейки для О ___ ___"))
        except:
            print("Убедитесь, что Вы ввели целое число")
            continue
        if inp in used:
            print("Эта ячейка уже использована. Выберите другую ячейку")
        else:
            if inp in range (0,9):
                result[inp] = "О"
                used.append(inp)
                valid = False

def print_():
    print("-----------")
    print("|", result[0], "|", result[1], "|", result[2] )
    print("-----------")
    print("|", result[3], "|", result[4], "|", result[5] )
    print("-----------")
    print("|", result[6], "|", result[7], "|", result[8] )
    print("-----------")

def check_():
    all_options = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in all_options:
        if result[i[0]] == result[i[1]] == result[i[2]]:
            return True

def play():
    print_()
    inp_player_1()
    if check_():
        print_()
        print("Победа Первого игрока. Выиграли 'крестики' ")
        return
    if all([type(x) is str for x in result]):
        print("Ничья")
        return
    print_()
    inp_player_2()
    if check_():
        print_()
        print("Победа Второго игрока. Выиграли 'нолики' ")
        return
    if all([type(x) is str for x in result]):
        print("Ничья")
        return
    play()

play()

