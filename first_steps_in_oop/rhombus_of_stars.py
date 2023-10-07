def print_rhombus(n):
    upper_triangle(n)
    lower_triangle(n)


def upper_triangle(n):
    for count in range(1, n + 1):
        print(" " * (n - count), end="")
        print(*["*"] * count)


def lower_triangle(n):
    for count in range(n - 1, 0, -1):
        print(" " * (n - count), end="")
        print(*["*"] * count)


n = int(input())

print_rhombus(n)
