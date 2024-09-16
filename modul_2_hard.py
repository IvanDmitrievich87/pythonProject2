def generate_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            pair_sum = i + j
            if n % pair_sum == 0:
                result += f'{i}{j}'
    return result


for k in range(1, 19):
    print(f'Ввод: {k}')
    n = int(input('Введите число от 3 до 20: '))
    if 3 <= n <= 20:
        password = generate_password(n)
        print(f'Пароль для {n}: {password}')
    else:
        print('Число должно быть от 3 до 20')