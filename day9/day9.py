def read_list():
    f = open("input.txt", "r")
    num = ""
    cont = 0
    toReturn = []
    for char in f.read():
        if char == ',':
            toReturn.append(int(num))
            num = ""
            cont = 0
        else:
            num += char
            cont += 1
    if cont != 0:
        toReturn.append(int(num))
    return toReturn


def do_operation(inp, i, opcode_full, rel_base):
    opcode = opcode_full % 100
    try:
        if opcode == 1:
            first_par_mode = (opcode_full % 1000) // 100
            second_par_mode = (opcode_full % 10000) // 1000
            third_par_mode = (opcode_full % 100000) // 10000
            if first_par_mode == 0:
                first_par = inp[inp[i + 1]]
            elif first_par_mode == 1:
                first_par = inp[i + 1]
            else:
                first_par = inp[inp[i + 1] + rel_base[0]]
            if second_par_mode == 0:
                second_par = inp[inp[i + 2]]
            elif first_par_mode == 1:
                second_par = inp[i + 2]
            else:
                second_par = inp[inp[i + 2] + rel_base[0]]
            if third_par_mode == 0:
                inp[inp[i + 3]] = first_par + second_par
            elif third_par_mode == 2:
                inp[inp[i + 3] + rel_base[0]] = first_par + second_par
            return i + 4
        elif opcode == 2:
            first_par_mode = (opcode_full % 1000) // 100
            second_par_mode = (opcode_full % 10000) // 1000
            third_par_mode = (opcode_full % 100000) // 10000

            if first_par_mode == 0:
                first_par = inp[inp[i + 1]]
            elif first_par_mode == 1:
                first_par = inp[i + 1]
            else:
                first_par = inp[inp[i + 1] + rel_base[0]]
            if second_par_mode == 0:
                second_par = inp[inp[i + 2]]
            elif first_par_mode == 1:
                second_par = inp[i + 2]
            else:
                second_par = inp[inp[i + 2] + rel_base[0]]
            if third_par_mode == 0:
                inp[inp[i + 3]] = first_par * second_par
            elif third_par_mode == 2:
                inp[inp[i + 3] + rel_base[0]] = first_par * second_par
            return i + 4
        elif opcode == 3:
            first_par_mode = (opcode_full % 1000) // 100
            if first_par_mode == 0:
                inp[inp[i + 1]] = int(input("Write an integer: "))
            elif first_par_mode == 2:
                inp[inp[i + 1] + rel_base[0]] = int(input("Write an integer: "))
            return i + 2
        elif opcode == 4:
            first_par_mode = (opcode_full % 1000) // 100
            if first_par_mode == 0:
                print(inp[inp[i + 1]])
            elif first_par_mode == 1:
                print(inp[i + 1])
            else:
                print(inp[inp[i + 1] + rel_base[0]])
            return i + 2
        elif opcode == 5:
            first_par_mode = (opcode_full % 1000) // 100
            second_par_mode = (opcode_full % 10000) // 1000

            if first_par_mode == 0:
                if inp[inp[i + 1]] != 0:
                    if second_par_mode == 0:
                        return inp[inp[i + 2]]
                    elif second_par_mode == 1:
                        return inp[i + 2]
                    else:
                        return inp[inp[i + 2] + rel_base[0]]
                else:
                    return i + 3
            elif first_par_mode == 1:
                if inp[i + 1] != 0:
                    if second_par_mode == 0:
                        return inp[inp[i + 2]]
                    elif second_par_mode == 1:
                        return inp[i + 2]
                    else:
                        return inp[inp[i + 2] + rel_base[0]]
                else:
                    return i + 3
            else:
                if inp[inp[i + 1] + rel_base[0]] != 0:
                    if second_par_mode == 0:
                        return inp[inp[i + 2]]
                    elif second_par_mode == 1:
                        return inp[i + 2]
                    else:
                        return inp[inp[i + 2] + rel_base[0]]
                else:
                    return i + 3
        elif opcode == 6:
            first_par_mode = (opcode_full % 1000) // 100
            second_par_mode = (opcode_full % 10000) // 1000
            if first_par_mode == 0:
                if inp[inp[i + 1]] == 0:
                    if second_par_mode == 0:
                        return inp[inp[i + 2]]
                    elif second_par_mode == 1:
                        return inp[i + 2]
                    else:
                        return inp[inp[i + 2] + rel_base[0]]
                else:
                    return i + 3
            elif first_par_mode == 1:
                if inp[i + 1] == 0:
                    if second_par_mode == 0:
                        return inp[inp[i + 2]]
                    elif second_par_mode == 1:
                        return inp[i + 2]
                    else:
                        return inp[inp[i + 2] + rel_base[0]]
                else:
                    return i + 3
            else:
                if inp[inp[i + 1] + rel_base[0]] == 0:
                    if second_par_mode == 0:
                        return inp[inp[i + 2]]
                    elif second_par_mode == 1:
                        return inp[i + 2]
                    else:
                        return inp[inp[i + 2] + rel_base[0]]
                else:
                    return i + 3
        elif opcode == 7:
            first_par_mode = (opcode_full % 1000) // 100
            second_par_mode = (opcode_full % 10000) // 1000
            third_par_mode = (opcode_full % 100000) // 10000
            if first_par_mode == 0:
                if second_par_mode == 0:
                    if inp[inp[i + 1]] < inp[inp[i + 2]]:
                        if third_par_mode == 0:
                            inp[inp[i+3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
                elif second_par_mode == 1:
                    if inp[inp[i + 1]] < inp[i + 2]:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
                else:
                    if inp[inp[i + 1]] < inp[inp[i + 2] + rel_base[0]]:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
            elif first_par_mode == 1:
                if second_par_mode == 0:
                    if inp[i + 1] < inp[inp[i + 2]]:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
                elif second_par_mode == 1:
                    if inp[i + 1] < inp[i + 2]:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
                else:
                    if inp[i + 1] < inp[inp[i + 2] + rel_base[0]]:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
            else:
                if second_par_mode == 0:
                    if inp[inp[i + 1] + rel_base[0]] < inp[inp[i + 2]]:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
                elif second_par_mode == 1:
                    if inp[inp[i + 1] + rel_base[0]] < inp[i + 2]:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
                else:
                    if inp[inp[i + 1] + rel_base[0]] < inp[inp[i + 2] + rel_base[0]]:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 1
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 1
                    else:
                        if third_par_mode == 0:
                            inp[inp[i + 3]] = 0
                        elif third_par_mode == 2:
                            inp[inp[i + 1] + rel_base[0]] = 0
            return i + 4
        elif opcode == 8:
            first_par_mode = (opcode_full % 1000) // 100
            second_par_mode = (opcode_full % 10000) // 1000
            if first_par_mode == 0:
                if second_par_mode == 0:
                    if inp[inp[i + 1]] == inp[inp[i + 2]]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
                elif second_par_mode == 1:
                    if inp[inp[i + 1]] == inp[i + 2]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
                else:
                    if inp[inp[i + 1]] == inp[inp[i + 2] + rel_base[0]]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
            elif first_par_mode == 1:
                if second_par_mode == 0:
                    if inp[i + 1] == inp[inp[i + 2]]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
                elif second_par_mode == 1:
                    if inp[i + 1] == inp[i + 2]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
                else:
                    if inp[i + 1] == inp[inp[i + 2] + rel_base[0]]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
            else:
                if second_par_mode == 0:
                    if inp[inp[i + 1] + rel_base[0]] == inp[inp[i + 2]]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
                elif second_par_mode == 1:
                    if inp[inp[i + 1] + rel_base[0]] == inp[i + 2]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
                else:
                    if inp[inp[i + 1] + rel_base[0]] == inp[inp[i + 2] + rel_base[0]]:
                        inp[inp[i + 3]] = 1
                    else:
                        inp[inp[i + 3]] = 0
            return i + 4
        elif opcode == 9:
            first_par_mode = (opcode_full % 1000) // 100
            if first_par_mode == 0:
                rel_base[0] += inp[inp[i + 1]]
            elif first_par_mode == 1:
                rel_base[0] += inp[i + 1]
            else:
                relative = rel_base[0]
                rel_base[0] += inp[i + 1 + relative]
            return i + 2
        elif opcode == 99:
            return -1
        else:
            return -1
    except IndexError:
        #print("Index oob")
        try:
            for j in range(inp[inp[i + 1]] - len(inp)):
                inp.append(0)
            return i
        except IndexError:
            #print("Another error")
            for j in range(i + 1):
                inp.append(0)
            return i


def part_one(inp, i, rel_base, finish):
    try:
        if i < finish:
            opcode_full = inp[i]
            length = do_operation(inp, i, opcode_full, rel_base)
            if length != -1 and opcode_full:
                part_one(inp, length, rel_base, finish)
    except RecursionError:
        print("Recursion finish")


inp = read_list()
for i in range(3):
    inp.append(0)
finish = len(inp)
part_one(inp, 0, [0], finish)
