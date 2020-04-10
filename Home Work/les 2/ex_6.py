# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента
# — номер товара и словарь с параметрами (характеристиками товара: название, цена, количество,
# единица измерения). Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ —
# характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
# Пример:
# {
#     “название”: [“компьютер”, “принтер”, “сканер”],
#     “цена”: [20000, 6000, 2000],
#     “количество”: [5, 2, 7],
#     “ед”: [“шт.”]
products_list = []
i = 1
while True:

    product = (i,{'name':None,'price':None,'amount':None,'unit':None})
    next_step = input('For exit press exit, for add product press add.\n')
    if next_step == 'exit':
        break
    elif next_step == 'add':
        press_name = input('Press product name:\n')
        product[1]['name'] = press_name
        press_price = input('Press product price:\n')
        product[1]['price'] = press_price
        press_amount = input('Press product amount:\n')
        product[1]['amount'] = press_amount
        press_unit = input('Press product unit:\n')
        product[1]['unit'] = press_unit
        products_list.append(product)
        i += 1
        print(products_list)


all_products = []
all_prices = []
all_amount = []
all_unit = []

for i in range(0,len(products_list)):
    all_products.append(products_list[i][1]['name'])
for i in range(0,len(products_list)):
    all_prices.append(products_list[i][1]['price'])
for i in range(0,len(products_list)):
    all_amount.append(products_list[i][1]['amount'])
for i in range(0,len(products_list)):
    all_unit.append(products_list[i][1]['unit'])

print(f'name : {all_products}')
print(f'price : {all_prices}')
print(f'amount : {all_amount}')
print(f'unit : {all_unit}')