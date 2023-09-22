tuple = (3, 5, 7, 8, 9, 2)
even_numbers = []

for num in tuple:
    if num % 2 == 0:
        even_numbers.append(num)

if len(even_numbers) > 0:
    print(min(even_numbers))
else:
    print(tuple[0])
