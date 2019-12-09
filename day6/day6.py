fileinp = open("input.txt", "r")

orbit_dic = {}
for line in fileinp.readlines():
    if line[0] != '\n':
        words = line.split(")")
        orbiter = words[1][:-1]
        orbit_dic[orbiter] = words[0]


def calculate_orbits(orbit_dic, key):
    if key in orbit_dic:
        if orbit_dic[key] == "COM":
            return 1
        else:
            return 1 + calculate_orbits(orbit_dic, orbit_dic[key])
    else:
        return 0


def calculate_transfers(orbit_dic, key, common_key):
    if key in orbit_dic:
        if orbit_dic[key] == common_key:
            return 0
        else:
            return 1 + calculate_transfers(orbit_dic, orbit_dic[key], common_key)
    else:
        return 0


num_orbits = 0
for key in orbit_dic:
    num_orbits += calculate_orbits(orbit_dic, key)


def find_all_orbits(key):
    if key in orbit_dic:
        if orbit_dic[key] == "COM":
            return ["COM"]
        else:
            return [orbit_dic[key]] + find_all_orbits(orbit_dic[key])
    else:
        return []


def find_common_point(you, san):
    me = find_all_orbits(you)
    santa = find_all_orbits(san)
    for orbit in me:
        if orbit in santa:
            return orbit
    return 0


print(find_all_orbits("YOU"))
print(find_all_orbits("SAN"))

print(find_common_point("YOU", "SAN"))

print(calculate_transfers(orbit_dic, "YOU", find_common_point("YOU", "SAN")) + calculate_transfers(orbit_dic, "SAN", find_common_point("YOU", "SAN")))
