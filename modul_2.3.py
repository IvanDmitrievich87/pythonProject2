my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0                              # начальный индекс
while index < len(my_list):            # оператор для перебора цикла текущих команд
    current_number = my_list[index]    # присваеваем переменной значение из списка по текущему индексу
    if current_number < 0:
        break                          # оператор для прирывания цикла команд, если срабатывает условие
    elif current_number > 0:
        print(current_number)
    index += 1