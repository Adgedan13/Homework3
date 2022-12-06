# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:

# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import random as r
random_list = [r.randint(1, 6) for i in range(r.randint(4, 8))]
print('Список случайных чисел:', random_list)
len_list = len(random_list)
mult_list = [random_list[i] * random_list[-i - 1] for i in range(len_list // 2)]
if len_list % 2 == 1:
    mult_list.append(random_lst[len_lst // 2] ** 2)
print('Список произведения пар чисел:', mult_list)