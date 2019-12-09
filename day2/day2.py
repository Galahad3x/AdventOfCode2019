def read_list():
    f = open("input.txt", "r")
    num = 0
    cont = 0
    toReturn = []
    for char in f.read():
        if char == ',':
            toReturn.append(num)
            num = 0
            cont = 0
        else:
            num *= 10
            num += int(char)
            cont += 1
    if cont != 0:
        toReturn.append(num)
    return toReturn


def do_operation(inp, i):
    opcode = inp[i]
    if opcode == 1:
        inp[inp[i + 3]] = inp[inp[i + 1]] + inp[inp[i + 2]]
        return True
    if opcode == 2:
        inp[inp[i + 3]] = inp[inp[i + 1]] * inp[inp[i + 2]]
        return True
    if opcode == 99:
        return False


def part_one(inp):
    i = 0
    while do_operation(inp, i):
        i += 4
    return inp[0]


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
inp[1] = 12
inp[2] = 2
print(part_one(inp))
print(part_two())
