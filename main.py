def get_shop_list_by_dishes(dishes, person_count):
    dic = {}
    for dish in dishes:
        for ings in cook_book[dish]:
            if ings["ingredient_name"] in dic.keys():
                dic[ings["ingredient_name"]]["quantity"] = str(int(dic[ings["ingredient_name"]]["quantity"]) * person_count)
            else:
                dic[ings["ingredient_name"]] = {"measure": ings["measure"], "quantity": str(int(ings["quantity"]) * person_count)}
    return dic


with open("recipes.txt", "rt", encoding= "utf8") as file:
    cook_book = {}
    for el in file:
        dish = el.strip()
        cook_book[dish] = []
        num_products = file.readline().strip()
        for i in range(int(num_products)):
            ingredients = {}
            ing = file.readline().strip()
            ingredient_name, quantity, measure = ing.split(" | ")
            ingredients["ingredient_name"] = ingredient_name
            ingredients["quantity"] = quantity
            ingredients["measure"] = measure
            cook_book[dish].append(ingredients)
        emp_line = file.readline()


print(cook_book)
print()
print(get_shop_list_by_dishes(["Омлет", "Запеченный картофель", "Фахитос"], 2))