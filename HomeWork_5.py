# task 1: Разделение списка
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

divisible_by_3 = []
divisible_by_5 = []
divisible_by_3_and_5 = []

for num in input_list:
    if num % 3 == 0 and num % 5 == 0:
        divisible_by_3_and_5.append(num)
    elif num % 3 == 0:
        divisible_by_3.append(num)
    elif num % 5 == 0:
        divisible_by_5.append(num)

print(divisible_by_3)
print(divisible_by_5)
print(divisible_by_3_and_5)

# task 2: Сумма и произведение элементов списка по условию
lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6

filtered_lst = [x for x in lst if MIN <= x <= MAX]

if filtered_lst:
    sum_ = sum(filtered_lst)
    product = 1
    for x in filtered_lst:
        product *= x
else:
    sum_ = 0
    product = 0

print('sum =', sum_)
print('product =', product)

# task 3: Добавление средних значений в список
lst = [3.5, 2, 4, 6.2, 8]
lst_2 = []

for i in range(len(lst)-1):
    lst_2.append(lst[i])
    avg = (lst[i] + lst[i+1])/2
    lst_2.append(avg)
lst_2.append(lst[-1])

print(lst_2)

# task 4: Сортировка колонок двумерного списка
matrix = [['a', 'c', 'd'], ['f', 'b', 'a'], ['a', 'n', 'k'], ['e', 'l', 'i']]
sorted_matrix = [sorted(col) for col in zip(*matrix)]
result = list(map(list, zip(*sorted_matrix)))

for row in result:
    print(row, sep='\n')




