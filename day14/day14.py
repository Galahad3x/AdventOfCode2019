import math

f = open("input.txt", "r")

ingredients = {}
inventory = {}
for line in f.readlines():
    ing = line.split(" => ")[0].split(", ")
    out = line.split(" => ")[1][:-1]
    ingredients[out] = ing
    inventory[out.split(" ")[1]] = 0

print(ingredients)
print(inventory)

objective = "1 FUEL"


def get_ore(objective):
    global ingredients
    global inventory
    objective_mineral = objective.split(" ")[1]
    objective_quantity = int(objective.split(" ")[0])
    if objective_quantity >= inventory[objective_mineral]:
        needed = objective_quantity - inventory[objective_mineral]
    else:
        return 0
    for key in ingredients.keys():
        if objective_mineral in key:
            real_key = key
            quantity_in_key = int(key.split(" ")[0])
            break
    n_of_reactions = math.ceil(needed / quantity_in_key)
    if n_of_reactions == 0:
        n_of_reactions = 1
    real_quantity = int(quantity_in_key * n_of_reactions)
    ing_needed = ingredients[real_key][:]
    print("Type: " + str(ing_needed))
    ingredients_needed = []
    for ingredient in ing_needed:
        quantity_in_recipe = int(ingredient.split(" ")[0])
        ingredients_needed.append(ingredient.replace(str(quantity_in_recipe), str(quantity_in_recipe * n_of_reactions)))
    if n_of_reactions == 0:
        raise Exception("Something went wrong")
    print("Type: " + str(ingredients_needed))
    ore = 0
    for ingredient in ingredients_needed:
        reactive_mineral = ingredient.split(" ")[1]
        reactive_quantity = int(ingredient.split(" ")[0])
        inventory[objective_mineral] += (real_quantity - objective_quantity)
        if reactive_mineral.__eq__("ORE"):
            ore += reactive_quantity
        else:
            ore += get_ore(ingredient)
    return ore


ing_needed = {}
result = get_ore(objective)
print(result)
