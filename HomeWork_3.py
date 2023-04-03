# task 1
a = int(input('Enter number: '))
b = int(input('Enter number: '))
c = int(input('Enter number: '))
print(max(a, b, c))

# task 2
height = int(input('Enter height of rectangular: '))   # Enter 3
width = int(input('Enter width of rectangular: '))  # Enter 6
special_symbol = input('Enter symbol to build rectangular with: ')  # Enter ^
row = special_symbol * width
for i in range(height):
    print(row)

# task 3
triangle_size = int(input("Enter size of triangle: "))    # Enter 5
for d in range(1, triangle_size + 1):
    for e in range(triangle_size - d):
        print(" ", end="")
    for e in range(d):
        print('*', end='')
    print()

# task 4



