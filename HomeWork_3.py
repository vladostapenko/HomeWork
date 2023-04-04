# task 1
a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
if a > b:
    if a > c:
        print(a)
    else:
        print(c)
else:
    if b > c:
        print(b)
    else:
        print(c)


# task 2
height = int(input('Enter height: '))   # Enter 3
width = int(input('Enter width: '))  # Enter 6
special_symbol = input('Enter symbol: ')  # Enter ^
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



