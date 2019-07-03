a = 1
b = 1

while b <= 1_000_000_000_000:
    a1 = 3 * a + 2 * b - 2
    b1 = 4 * a + 3 * b - 3
    a = a1
    b = b1

print(a)
print(b)
