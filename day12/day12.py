f = open("example2.txt", "r")


class Moon:
    coordinates = []
    velocity = []

    def __init__(self, coordinates, velocity):
        self.coordinates = coordinates
        self.velocity = velocity

    def __eq__(self, other):
        return self.coordinates.__eq__(other.coordinates) and self.velocity.__eq__(other.velocity)

    def add_vel(self):
        for i in range(len(self.coordinates)):
            self.coordinates[i] += self.velocity[i]

    def energy(self):
        potential = 0
        kinetic = 0
        for i in range(len(self.coordinates)):
            potential += abs(self.coordinates[i])
            kinetic += abs(self.velocity[i])
        return potential * kinetic


moons = []
for line in f.readlines():
    coordinates = []
    for data in line.split(","):
        coordinates.append(int(data))
    moons.append(Moon(coordinates, [0, 0, 0]))

f.close()

for step in range(1000):
    # Calculating velocities
    for moon in moons:
        for moon2 in moons:
            if not moon.__eq__(moon2):
                for i in range(len(moon.coordinates)):
                    if moon.coordinates[i] > moon2.coordinates[i]:
                        moon.velocity[i] -= 1
                    elif moon.coordinates[i] < moon2.coordinates[i]:
                        moon.velocity[i] += 1

    # Adding velocities
    for moon in moons:
        moon.add_vel()

total_energy = 0
for moon in moons:
    print(moon.energy())
    total_energy += moon.energy()

print(total_energy)


class State:
    moons = []

    def __init__(self, moons):
        self.moons = moons

    def __eq__(self, other):
        for i in range(len(self.moons)):
            if not self.moons[i].__eq__(other.moons[i]):
                return False
        return True


f = open("example2.txt", "r")

# Reset to original data
moons = []
for line in f.readlines():
    coordinates = []
    for data in line.split(","):
        coordinates.append(int(data))
    moons.append(Moon(coordinates, [0, 0, 0]))

states = [moons[:]]
steps = 0
while True:
    # Calculating velocities
    for moon in moons:
        for moon2 in moons:
            if not moon.__eq__(moon2):
                for i in range(len(moon.coordinates)):
                    if moon.coordinates[i] > moon2.coordinates[i]:
                        moon.velocity[i] -= 1
                    elif moon.coordinates[i] < moon2.coordinates[i]:
                        moon.velocity[i] += 1

    # Adding velocities
    for moon in moons:
        moon.add_vel()

    eq = True
    for state in states:
        eq = True
        for i in range(len(state)):
            if not moons[i].__eq__(state[i]):
                eq = False
        if eq:
            break

    if eq:
        break
    states.append(moons[:])
    steps += 1
    print(steps)

print(steps)
