numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for number in numbers:             # оператор, который создаёт цикл для перебора повторений, которые мы сами определили
    if number < 2:
          continue                 # оператор возращающий в начало цикла
    is_prime = True                # переменный флаг
# Вложеный цикл для проверки делителей
    for i in range(2, int(number ** 0.5) + 1): # число в степени 0,5 эквивалентно извлечению квадратного корня
                                               # range - возрвращает последовательность чисел
        if number % i == 0:
            is_prime = False       # переменный флаг
            break                  # выходим из цикла
    if is_prime:
        primes.append(number)      # append - команда позволяющая добовлять поочерёдно элементы одного списка в другой
    else:
        not_primes.append(number)
print('Primes:', primes)
print('Not Primes:', not_primes)