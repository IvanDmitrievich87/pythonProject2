first = int(input('Введите число: '))                      #input - команда для ввода с клавиатуру
second = int(input('Введите число: '))
third  = int(input('Введите число: '))
if first == second == third:                               # if - блок условий
    print(3)                                               # Все три числа равны
elif first == second or second == third or first == third: # elif - блок условий
    print(2)                                               # Хотя бы два числа равны
else:                                                      # else - блок условий
    print(0)                                               # Равных чисел нет