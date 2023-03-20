from pprint import pprint

# Задача 1
f = open('recipes.txt', 'r', encoding='utf-8')
cook_book = {}
for line in f:
    dish = line.strip()
    ing_count = int(f.readline().strip())
    ingredients = []
    for _ in range(ing_count):
        ingredient, quantity, measure = f.readline().strip().split(' | ')
        ingredients.append({
            'ingredient_name': ingredient,
            'quantity': int(quantity),
            'measure': measure
        })
    f.readline()
    cook_book[dish] = ingredients

f.close()
pprint(cook_book, sort_dicts=False)


# Задача 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            i = {ing['ingredient_name']: {'measure': ing['measure'], 'quantity': ing['quantity'] * person_count}}
            for k, v in shop_list.items():
                for key, value in i.items():
                    if k == key:
                        value['quantity'] += v['quantity']
            shop_list.update(i)
    return shop_list


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), sort_dicts=False)

# Задача 3


def combine_sorted_files():
    list_files_in_dir = ['1.txt', '2.txt', '3.txt']
    string_from_files = []
    for file in list_files_in_dir:
        with open(file, 'r', encoding='utf-8') as f:
            temp = []
            for line in f:
                temp.append(line.strip())
            temp.insert(0, str(len(temp)))
            temp.insert(0, file)
            string_from_files.append(temp)
    string_from_files.sort(key=len)
    file = 'comb_text.txt'
    with open(file, 'w', encoding='utf-8') as f:
        for string in string_from_files:
            for i in string:
                f.writelines(i + '\n')
    return


combine_sorted_files()