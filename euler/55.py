def is_lychrel(n):
    for i in range(0, 50):
        n = int(str(n)[::-1]) + n
        if str(n)[::-1] == str(n):
            return False
    return True
        
         

def main():
    count = 0
    for i in range(1, 10000):
        if is_lychrel(i):
            print ("%d" % i)
            count = count + 1
    print (count)

if __name__ == '__main__':
    main()
  
