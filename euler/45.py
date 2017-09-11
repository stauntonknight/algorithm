import math

def is_penta(n):
    x = 1 + math.sqrt(24 * n + 1)
    return x % 6 == 0

def is_triangle(n):
    target = n * 2
    x = int(math.sqrt(target))
    return x * (x + 1) == target


i = 0
while True:
    i = i + 1
    target = i * (2 * i - 1)
    if is_triangle(target) and is_penta(target):
        print(target)
        
        
