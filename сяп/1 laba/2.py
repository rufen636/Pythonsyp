# Вводим строку с клавиатуры
s = input("Введите строку: ")

# Разбиваем строку на слова и подсчитываем количество слов с четной длиной
words = s.split()
even_len_words = [word for word in words if len(word) % 2 == 0]
print(f"Количество слов с четной длиной: {len(even_len_words)}")

# Считаем частоту вхождения каждой буквы
freq = {}
for letter in s:
    if letter.isalpha():
        freq[letter] = freq.get(letter, 0) + 1

# Выводим результаты
print("Частота вхождения каждой буквы:")
for letter, count in freq.items():
    print(f"{letter}: {count}")
