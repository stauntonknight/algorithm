import math

def main():
    summax = 0
    for a in range(1, 101):
        for b in range(1, 101):
            num = str(a ** b)
            sumt = sum(int(digit) for digit in num)
            if sumt > summax:
                summax = sumt
    print(summax)
           
if __name__ == '__main__':
    main()
