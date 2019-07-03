from math import sqrt

b = 1

kount = 0

while 3 * b + 1 <= 1000000000:
    x = 3 * b + 1
    y = b - 1
    z = b + 1
    t = sqrt(x * y) 
    area = t * z
    if area % 4 == 0:
        kount += 1
    b += 1

print("done one")
b = 1
while 3 * b - 1 <= 1000000000:
    x = 3 * b - 1
    y = b + 1
    z = b - 1
    t = sqrt(x * y) 
    area = t * z
    if area % 4 == 0:
        kount += 1
    b += 1

print(kount)

