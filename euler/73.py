import fractions

num = 1
den = 1
count = 0
sum = 0

while den <= 12000:
    count = 0
    min_num = int((den + 0.0) / 3 + 1)
    max_num = den/2 
    if den % 2 == 0:
        max_num -= 1
    while min_num <= max_num:
        if fractions.gcd(min_num, den) == 1:
            count += 1
        min_num += 1
    sum += count
    den += 1
print(sum)
