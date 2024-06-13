num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
num4 = float(input("Введіть четверте число: "))

result_list = []
result_list.append(num1 + num2 + num3 + num4)  # Додавання
result_list.append(num1 - num2 - num3 - num4)  # Віднімання
result_list.append(num1 * num2 * num3 * num4)  # Множення
result_list.append(num1 / num2 / num3 / num4)  # Ділення
result_list.append(num1 ** num2)  # Піднесення до ступеня
result_list.append(num1 // num2)  # Цілочисельне ділення
result_list.append(num1 % num2)  # Остача від ділення

print("Кількість елементів у списку:", len(result_list))
print("Парні елементи списку:")
for i in range(len(result_list)):
    if result_list[i] % 2 == 0:
        print(result_list[i])

temp = result_list[1]
result_list[1] = result_list[4]
result_list[4] = temp
print("Список після заміни другого і п'ятого елементів:")
print(result_list)

name = input("Введіть ваше прізвище та ім'я: ")
print(f"Лабораторну роботу виконав {name}.")
print("Висновки:")
print("У цій лабораторній роботі ми вивчили основні операції з числами у Python.")
print("Ми також навчилися працювати зі списками та змінними.")5