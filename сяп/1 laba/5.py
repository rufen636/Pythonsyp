# заданный словарь
shop_dict = {
    'рулевая рейка': ['рулевая рейка', 'цена: 5000 руб.', 'количество: 10 шт.'],
    'диски': ['диски', 'цена: 2000 руб.', 'количество: 20 шт.'],
    'шины': ['шины', 'цена: 3000 руб.', 'количество: 30 шт.'],
    'фильтр масляный': ['фильтр масляный', 'цена: 500 руб.', 'количество: 50 шт.'],
    'фильтр воздушный': ['фильтр воздушный', 'цена: 300 руб.', 'количество: 100 шт.'],
    'масло моторное': ['масло моторное', 'цена: 1000 руб.', 'количество: 40 шт.']
}

while True:
    print('Меню:\n1. Просмотр описания\n2. Просмотр цены\n3. Просмотр количества\n4. Вся информация \n5. Покупка \n6. До свидания')

    choice = input('Введите номер пункта меню: ')

    if choice == '1':
        item = input('Введите название продукции: ')
        print(shop_dict[item][0])

    elif choice == '2':
        item = input('Введите название продукции: ')
        print(shop_dict[item][1])

    elif choice == '3':
        item = input('Введите название продукции: ')
        print(shop_dict[item][2])

    elif choice == '4':
        for key, value in shop_dict.items():
            print(key + ': ' + ', '.join(value))

    elif choice == '5':
        total_price = 0
        while True:
            item = input('Введите название продукции (n - выход): ')
            if item == 'n':
                break
            if item not in shop_dict:
                print('Такой продукции нет в магазине')
                continue
            quantity = int(input('Введите количество: '))
            if quantity > int(shop_dict[item][2].split(': ')[1].split()[0]):
                print('Недостаточно товара на складе')
                continue
            price = int(shop_dict[item][1].split(': ')[1].split()[0])
            total_price += price * quantity
            shop_dict[item][2] = 'количество: ' + \
                str(int(shop_dict[item][2].split(': ')[
                    1].split()[0]) - quantity) + ' шт.'
        print('Общая стоимость покупки:', total_price)

    elif choice == '6':
        print('До свидания!')
        break

    else:
        print('Некорректный ввод, попробуйте еще раз')
