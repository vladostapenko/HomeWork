# task 1
pets = ['Murzik', 'Barsik', 'Pantera']
print(*pets, sep=', ', end='\n\n')


# task 2
country = ['Ukraine', 'Spain', 'Italy']
capital = {'Ukraine': 'Kyiv', 'Spain': 'Madrid', 'Italy': 'Rome'}

for country, capital in capital.items():
    print(country + ': ' + capital)
print()


# task 3
a = int(input('Enter a: '))  # Enter 3
b = int(input('Enter b: '))  # Enter 5
sum_a_b = a + b
prod = a * b
print(a, '+', b, '=', sum_a_b)
print(a, '*', b, '=', prod)
