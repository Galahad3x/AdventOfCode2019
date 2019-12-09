f = open("input.txt", "r")

layers = []
line = f.read()

wide_counter = 0
tall_counter = 0
pixel_line = []
layer = []
for char in line:
    if char != '\n':
        if len(pixel_line) < 25:
            pixel_line.append(int(char))
        else:
            if len(layer) < 6:
                layer.append(pixel_line[:])
                # print("Line " + str(pixel_line))
                # print("Line length " + str(len(pixel_line)))
                tall_counter += 1
            else:
                layers.append(layer[:])
                layer = [pixel_line[:]]
                # print("Layer: " + str(layer) + str(len(layer)))
                tall_counter = 0
            pixel_line = [int(char)]

layer.append(pixel_line[:])
layers.append(layer[:])

min_0 = 25 * 6
out = 0
for layer in layers:
    number_of_0 = 0
    for row in layer:
        for pixel in row:
            if pixel == 0:
                number_of_0 += 1
    if number_of_0 < min_0:
        min_0 = number_of_0
        number_of_1 = 0
        number_of_2 = 0
        for row in layer:
            for pixel in row:
                if pixel == 1:
                    number_of_1 += 1
                if pixel == 2:
                    number_of_2 += 1
        out = number_of_1 * number_of_2

print(out)

image = [[2 for x in range(25)] for y in range(6)]

for layer in layers:
    for row_i in range(len(layer)):
        for pixel_i in range(len(layer[row_i])):
            if image[row_i][pixel_i] == 2:
                image[row_i][pixel_i] = layer[row_i][pixel_i]

for row in image:
    for elem in row:
        if elem == 1:
            print('#', end=' ')
        else:
            print(' ', end=' ')
    print('')

