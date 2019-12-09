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


def do_operation(inp, i, opcode_full):
    opcode = opcode_full % 100
    if opcode == 1:
        first_par_mode = (opcode_full % 1000) // 100
        second_par_mode = (opcode_full % 10000) // 1000
        if first_par_mode == 0:
            first_par = inp[inp[i + 1]]
        else:
            first_par = inp[i + 1]
        if second_par_mode == 0:
            second_par = inp[inp[i + 2]]
        else:
            second_par = inp[i + 2]
        inp[inp[i + 3]] = first_par + second_par
        return i + 4
    elif opcode == 2:
        first_par_mode = (opcode_full % 1000) // 100
        second_par_mode = (opcode_full % 10000) // 1000
        if first_par_mode == 0:
            first_par = inp[inp[i + 1]]
        else:
            first_par = inp[i + 1]
        if second_par_mode == 0:
            second_par = inp[inp[i + 2]]
        else:
            second_par = inp[i + 2]
        inp[inp[i + 3]] = first_par * second_par
        return i + 4
    elif opcode == 3:
        inp[inp[i + 1]] = int(input("Write an integer: "))
        return 2
    elif opcode == 4:
        first_par_mode = (opcode_full % 1000) // 100
        if first_par_mode == 0:
            print(inp[inp[i + 1]])
        else:
            print(inp[i + 1])
        return i + 2
    elif opcode == 5:
        first_par_mode = (opcode_full % 1000) // 100
        second_par_mode = (opcode_full % 10000) // 1000
        if first_par_mode == 0:
            if inp[inp[i + 1]] != 0:
                return -(second_par_mode - 1) * inp[inp[i + 2]] + second_par_mode * inp[i + 2]
            else:
                return i + 3
        else:
            if inp[i + 1] != 0:
                return -(second_par_mode - 1) * inp[inp[i + 2]] + second_par_mode * inp[i + 2]
            else:
                return i + 3
    elif opcode == 6:
        first_par_mode = (opcode_full % 1000) // 100
        second_par_mode = (opcode_full % 10000) // 1000
        if first_par_mode == 0:
            if inp[inp[i + 1]] == 0:
                return -(second_par_mode - 1) * inp[inp[i + 2]] + second_par_mode * inp[i + 2]
            else:
                return i + 3
        else:
            if inp[i + 1] == 0:
                return -(second_par_mode - 1) * inp[inp[i + 2]] + second_par_mode * inp[i + 2]
            else:
                return i + 3
    elif opcode == 7:
        first_par_mode = (opcode_full % 1000) // 100
        second_par_mode = (opcode_full % 10000) // 1000
        if first_par_mode == 0:
            if second_par_mode == 0:
                if inp[inp[i + 1]] < inp[inp[i + 2]]:
                    inp[inp[i + 3]] = 1
                else:
                    inp[inp[i + 3]] = 0
            else:
                if inp[inp[i + 1]] < inp[i + 2]:
                    inp[inp[i + 3]] = 1
                else:
                    inp[inp[i + 3]] = 0
        else:
            if second_par_mode == 0:
                if inp[i + 1] < inp[inp[i + 2]]:
                    inp[inp[i + 3]] = 1
                else:
                    inp[inp[i + 3]] = 0
            else:
                if inp[i + 1] < inp[i + 2]:
                    inp[inp[i + 3]] = 1
                else:
                    inp[inp[i + 3]] = 0
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
            else:
                if inp[inp[i + 1]] == inp[i + 2]:
                    inp[inp[i + 3]] = 1
                else:
                    inp[inp[i + 3]] = 0
        else:
            if second_par_mode == 0:
                if inp[i + 1] == inp[inp[i + 2]]:
                    inp[inp[i + 3]] = 1
                else:
                    inp[inp[i + 3]] = 0
            else:
                if inp[i + 1] == inp[i + 2]:
                    inp[inp[i + 3]] = 1
                else:
                    inp[inp[i + 3]] = 0
        return i + 4
    elif opcode == 99:
        return -1
    else:
        return 0


def part_one(inp, i):
    opcode_full = inp[i]
    length = do_operation(inp, i, opcode_full)
    if length != -1:
        part_one(inp, length)


def part_two():
    for noun in range(0, 100):
        for verb in range(0, 100):
            inp = read_list()
            inp[1] = noun
            inp[2] = verb
            print(part_one(inp))
            if part_one(inp) == 19690720:
                return 100 * noun + verb
    raise Exception('Desired output can not be achieved')


inp = read_list()
part_one(inp, 0)
