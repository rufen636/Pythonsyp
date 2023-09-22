# заданный список чисел
lst = [1, 2, 3, 4, 5, 2, 6, 4, 8, 9, 1]
print(lst)
# создаем словарь, где ключ - число из списка, значение - количество его вхождений
count_dict = {}
for num in lst:
    count_dict[num] = count_dict.get(num, 0) + 1

# считаем количество пар элементов, равных друг другу
pair_count = 0
for num in count_dict.values():
    if num > 1:
        pair_count += num * (num - 1) // 2

# выводим результат
print(f"Количество пар элементов, равных друг другу: {pair_count}")
