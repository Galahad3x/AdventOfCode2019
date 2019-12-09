from itertools import permutations
import sys


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


def read_list_2():
    f = open("input.txt", "r")
    toReturn = []
    for num in f.read().split(","):
        toReturn.append(int(num))
    return toReturn


def do_operation(inp, i, opcode_full, results, elem, output):
    global cont
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
        # inp[inp[i + 1]] = int(input("Write an integer: "))
        if cont == 0:
            inp[inp[i + 1]] = elem
            cont += 1
        else:
            inp[inp[i + 1]] = output
            cont += 1
        return i + 2
    elif opcode == 4:
        first_par_mode = (opcode_full % 1000) // 100
        if first_par_mode == 0:
            results.append(inp[inp[i + 1]])
            # print(inp[inp[i + 1]])
        else:
            results.append(inp[i + 1])
            # print(inp[i + 1])
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


def do_operation_2(inp, i, opcode_full, results, outputf):
    global cont
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
        # inp[inp[i + 1]] = int(input("Write an integer: "))
        if cont == 0:
            inp[inp[i + 1]] = elem
            cont += 1
        else:
            inp[inp[i + 1]] = output
            cont += 1
        return i + 2
    elif opcode == 4:
        first_par_mode = (opcode_full % 1000) // 100
        if first_par_mode == 0:
            outputf.write(str(inp[inp[i + 1]]) + "\n")
            print(inp[inp[i + 1]])
        else:
            outputf.write(str(inp[i + 1]) + "\n")
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
        return -1


def part_one(inp, i, results, elem, output):
    opcode_full = inp[i]
    length = do_operation(inp, i, opcode_full, results, elem, output)
    if length != -1:
        part_one(inp, length, results, elem, output)


permutationl = list(permutations([0, 1, 2, 3, 4]))

list_of_results = []
max_out = 0
max_perm = 0
for perm in permutationl:
    output = 0
    for elem in perm:
        cont = 0
        inp = read_list_2()
        part_one(inp, 0, list_of_results, elem, output)
        output = list_of_results[-1]
    if output > max_out:
        max_out = output
        max_perm = perm

#print(max_perm)
#print(max_out)

permutationl = list(permutations([5, 6, 7, 8, 9]))


def part_two(inp, i, elem, outputf):
    opcode_full = inp[i]
    length = do_operation_2(inp, i, opcode_full, elem, outputf)
    if length != -1:
        part_two(inp, length, elem, outputf)


f = open("out.txt", "w+")

inp = read_list_2()
for elem in permutationl[0]:
    print("Elem: " + str(elem))
    part_two(inp, 0, elem, f)
