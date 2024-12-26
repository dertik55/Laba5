# Ввод трех действительных чисел
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))

# Создание списка чисел
numbers = [a, b, c]

# Фильтрация чисел по модулю
filtered_numbers = [num for num in numbers if abs(num) >= 4]

# Вывод результата
print("Числа, модули которых не меньше 4:", filtered_numbers)
