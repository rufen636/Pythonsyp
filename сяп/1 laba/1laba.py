
# Создаем словарь соответствия годов животным знакам
animal_years = {}
animal_years = {0: 'Обезьяна', 1: 'Петух', 2: 'Собака', 3: 'Свинья', 4: 'Крыса',
                5: 'Бык', 6: 'Тигр', 7: 'Кролик', 8: 'Дракон', 9: 'Змея', 10: 'Лошадь', 11: 'Овца'}

# Создаем словарь соответствия годов элементам
element_years = {}
element_years = {0: 'Металл', 1: 'Вода', 2: 'Дерево', 3: 'Огонь', 4: 'Земля'}

# Создаем функцию для определения года по китайскому календарю


def chinese_zodiac(year):
    if year < 0:
        return "Введите положительное число"
    animal = animal_years[year % 12]
    element = element_years[(year // 2) % 5]
    return f"{animal}, {element} год"


# Запускаем цикл для ввода годов
while True:
    try:
        year = int(input("Введите год по китайскому календарю (0 для выхода): "))
        if year == 0:
            break
        print(chinese_zodiac(year))
    except ValueError:
        print("Введите целое число")
