from pprint import pprint
with open('recipes.txt', encoding='UTF-8') as file:
    cook_book = {}
    for line in file:
        ingredient_name = line.strip()
        ingredient_count = int(file.readline())
        ingredient = []
        for _ in range(ingredient_count):
            rec = file.readline().strip()
            name, count, ed_izm = rec.split('|')
            ingredient.append({
                'ingredient_name': name,
                'quantity': count, 
                'measure': ed_izm}
                )
        cook_book[ingredient_name] = ingredient
        file.readline()
pprint(cook_book, sort_dicts=False)
print()


def get_shop_list_by_dishes(dishes, person_count):
        cooking_list = {}
        for dish in dishes:
            if dish in cook_book:
                for ingr in cook_book[dish]:
                    if ingr['ingredient_name'] not in cooking_list:
                        value = {'quantity': int(ingr['quantity']) * person_count, 'measure': ingr['measure']}
                        cooking_list[ingr['ingredient_name']] = value
                    else:
                        cooking_list[ingr['ingredient_name']]['quantity'] += int(ingr['quantity']) * person_count

        return cooking_list
pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))