import math
import sympy
def get_factor(n):
    return sympy.factorint(n)
def main():
    count = 0
    min = 2 * 3 * 5 * 7
    while True:
        if len(sympy.factorint(min)) == 4:
            count = count + 1
        else:
            count = 0
        if count == 4:
            print ("%d" % (min - 3))
            print(sympy.factorint(min - 3))
            break
        min = min + 1

if __name__ ==  '__main__':
    main()
