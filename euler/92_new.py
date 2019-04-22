from functools import reduce

def squaredigits(n): # sum of the squares of the digits of n
    return(sum(int(x)**2 for x in str(n)))                               
def fact(n): #factorial n
    if n == 0: return(1)
    x = reduce(lambda a,b:a*b, range(1,n+1))
    return(x)
def permute(n): # the number of permutations of n
    x = set(n)
    y = fact(len(n))
    for a in x:
        y = y/fact(n.count(a))
    return(y)    
def converge(n): # what does n converge to?
    while n != 1 and n != 89:
        n = squaredigits(n)
    return(n)
def converge2(n,set1): # same result as converge(n)
    if squaredigits(n) in set1: return(1)
    else: return(2)  
set1 = set(filter(lambda n:converge(n) == 1,range(1,568)))# set1 converges to 1
count = 0
for a in range(10):
    for b in range(a,10):
        for c in range(b,10):
            for d in range(c,10):
                for e in range(d,10):
                    for f in range(e,10):
                        for g in range(max(f,1),10):
                            x = [str(t) for t in [a,b,c,d,e,f,g]]
                            y = "".join(x)
                            y = int(y)
                            if converge2(y,set1) == 1:
                                count += permute(x)
print((10**7 -1) - count)
