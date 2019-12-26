# part 1

f = open("input.txt", "r")

inp = []
for elem in f.read():
    if elem != '\n':
        inp.append(int(elem))


def cut(to_cut):
    if to_cut[0] == 0:
        return cut(to_cut[1:])
    else:
        return to_cut


def offseted_pattern(pattern, index, len_needed):
    pat = []
    pattern_element_counter = 0
    pattern_repeated_counter = 0
    while len(pat) <= len_needed:
        # print("calculating offseted pattern " + str(len(pat)))
        if pattern_repeated_counter <= index:
            pat.append(pattern[pattern_element_counter])
            pattern_repeated_counter += 1
        else:
            pattern_element_counter = (pattern_element_counter + 1) % len(pattern)
            pattern_repeated_counter = 0
    return pat[1:]


def FFT_phase(input_of_FFT):
    pattern = [0, 1, 0, -1]
    final_inp = []
    for i, elem in enumerate(input_of_FFT):
        mypat = offseted_pattern(pattern, i, len(input_of_FFT))
        print("calculating elem in phase " + str(i))
        calculated_number = 0
        for j in range(len(input_of_FFT)):
            if mypat[j] != 0:
                calculated_number += (input_of_FFT[j] * mypat[j]) % 10
        final_inp.append(abs(calculated_number) % 10)

    return final_inp


def index_of_pattern(pos, posc):
    return (pos // posc) % 4


def FFT_phase_2(input_of_FFT):
    pattern = [0, 1, 0, -1]
    final_inp = []
    for i, elem in enumerate(input_of_FFT):
        print("calculating elem in phase " + str(i))
        calculated_number = 0
        for j in range(len(input_of_FFT)):
            ind = index_of_pattern(j+1, i+1)
            if ind != 2 or ind != 0:
                calculated_number += input_of_FFT[j] * pattern[ind]
        final_inp.append(abs(calculated_number) % 10)

    return final_inp


print(inp)
for p in range(100):
    inp = FFT_phase_2(inp)
    print("calculating phase " + str(p))

for c in range(8):
    print(inp[c], end="")
print("")

# Part 2
f = open("input.txt", "r")

inp = []
mess_offset = 0
for count, elem in enumerate(f.read()):
    if elem != '\n':
        inp.append(int(elem))
    if count < 7:
        mess_offset *= 10
        mess_offset += int(elem)

signal = inp[:]
for k in range(10000):
    signal.extend(inp)
    print("extending " + str(k))
print(len(signal))

for p in range(100):
    signal = FFT_phase_2(signal)
    print("calculating phase " + str(p))

for c in range(8):
    print(inp[c + mess_offset], end="")
print("")
