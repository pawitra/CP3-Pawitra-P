num = int(input())
space = num

for i in range(num):
    space -= 1
    print(" " * space, "*" * ((i * 2) + 1))
