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


analitycs = {}

for key in product[1]:
    analitycs[key] = []

for i in range(len(products_list)):
    analitycs['name'].append(products_list[i][1]['name'])
    analitycs['price'].append(products_list[i][1]['price'])
    analitycs['amount'].append(products_list[i][1]['amount'])
    if products_list[i][1]['unit'] not in analitycs['unit']:
        analitycs['unit'].append(products_list[i][1]['unit'])

print(analitycs)