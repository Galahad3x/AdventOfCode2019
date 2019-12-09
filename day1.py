import math


def calculate_fuel(mass):
    return math.floor(mass / 3) - 2


def part_one(masses):
    fuels = []
    for mass in masses:
        fuel = calculate_fuel(mass)
        fuels.append(fuel)

    total_fuel_req = sum(fuels)
    return total_fuel_req


def total_fuel(mass):
    if calculate_fuel(mass) <= 0:
        return 0
    else:
        return calculate_fuel(mass) + total_fuel(calculate_fuel(mass))


def part_two(masses):
    fuels = []
    for mass in masses:
        fuel = total_fuel(mass)
        fuels.append(fuel)

    total_fuel_req = sum(fuels)
    return total_fuel_req


inp = open("input.txt", "r")

masses = []
for line in inp.readlines():
    mass = int(line)
    masses.append(mass)

print(part_one(masses))
print(part_two(masses))
