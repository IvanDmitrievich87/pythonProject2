def get_matrix(n, m, value):
    if n <= 0 or m <= 0:                       # Проверка на случаи, когда n или m меньше или равны 0
        return []                              # Возвращаем пустой список
    matrix = []                                # Создаем пустой список для матрицы
    for i in range(n):                         # Внешний цикл для строк матрицы
        matrix.append([])                      # Добавляем список n - строк в матрицу
        for j in range(m):
            matrix[i].append(value)            # Добовляем значение value для текущей строки i
    return matrix                              # Возращаем созданую матрицу

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(2, 4, 13)
print(result1)
print(result2)
print(result3)