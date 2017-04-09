from sympy import isprime

def gen_num():
    num_prime = 0
    total_num = 0
    last = 1
    total_num += 1
    step = 0;
    done = False 
    while not done:
        step += 2
        for i in range(0,4):
            last = last + step
            if (isprime(last)):
                num_prime += 1
            total_num += 1
            if num_prime * 10 <= total_num:
                print("Done")
                print(step)
                done = True
                break

gen_num()

