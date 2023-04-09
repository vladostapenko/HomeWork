# #  task 1
# a = int(input("Enter number: "))
# b = int(input("Enter number: "))
# c = int(input("Enter number: "))
# if a > b:
#     if a > c:
#         print(a)
#     else:
#         print(c)
# else:
#     if b > c:
#         print(b)
#     else:
#         print(c)
#
# # task 2
# height = int(input('Enter height: '))   # Enter 3
# width = int(input('Enter width: '))  # Enter 6
# special_symbol = input('Enter symbol: ')  # Enter ^
# row = special_symbol * width
# for i in range(height):
#     print(row)
#
# # task 3
# triangle_size = int(input("Enter size of triangle: "))    # Enter 5
# for d in range(1, triangle_size + 1):
#     for e in range(triangle_size - d):
#         print(" ", end="")
#     print()
#     for e in range(d):
#         print('*', end='')


# task 4
min_width = int(input("Enter minimal width: "))
max_width = int(input("Enter maximal width: "))

if min_width > max_width:
    print("Warning: Minimal width can't be greater than maximal width.")
elif (max_width - min_width) % 2 != 0:
    print("Warning: The difference between maximal and minimal width must be even.")
else:
    for i in range(min_width, max_width + 1, 2):
        spaces = (max_width - i) // 2
        if i == min_width:
            print(" " * spaces + "*" * i)
        else:
            print(" " * spaces + "*" + " " * (i-2) + "*")
    for i in range(max_width - 2, min_width - 1, -2):
        spaces = (max_width - i) // 2
        if i == min_width:
            print(" " * spaces + "*" * i)
        else:
            print(" " * spaces + "*" + " " * (i-2) + "*")

# task 5
height = int(input("Enter n: "))
for i in range(1, height + 1):
    print(" " * (2 * (height - i)), end="")
    for j in range(1, i + 1):
        print(" " + str(j), end="")
    for k in range(i - 1, 0, -1):
        print(" " + str(k), end="")
    print()
print("----"*height)

# task 5, another variant

lines = []
for l in range(1, height + 1):
    line = []
    for i in range(1, l + 1):
        line.append(i)
    for i in range(l, 1, -1):
        line.append(i - 1)
    lines.append(line)

for i in range(len(lines)):
    print("  " * (height-1-i), end="")
    print(*lines[i])
