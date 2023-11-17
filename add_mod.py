
import math
import random

c_int = 1.2
rmax = 10
a, n, P, Q, F, I2 = 0, 0, 0, 0, 0, 0
i, g, r = 0, 0, 0
success = False
P0 = 10000000
FactorList = [0] * rmax
ReSizeList = [0.0] * rmax



def Sqrt(a):
    return int(math.sqrt(a))

def Exponentiate(a, e):
        return int(a ** e)

def PrimeTest(a):
        if a < 2:
            return False
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True

def TrialDivision(a):
        if a < 2:
            return False
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True

def GenerateSizeList(sizeList):
    c = 1
    while True:
        u = random.uniform(0, c)
        sizeList.append(u)
        c = c - u
        sizeList.sort(reverse=True)
        
        for i in range(len(sizeList)):
            if sizeList[i] > 1 - sum(sizeList[0:i+1]):
                return sizeList[0:i+1]


def Checklemma1(n,a ,factorList):
    if (math.pow(a, n-1)) % n != 1:
        return False

    for q in factorList:
        if math.gcd(a**((n-1)//q) - 1, n) != 1:
            return False
    return True
        


def execute(P1, P2):
    if P2 <= P0:
        while True:
            n = random.randint(P1, P2)
            if PrimeTest(n):
                break
        return n
    else:

        F = 1
        p = (Sqrt((P1 - 1) * (P2 - 1))) / 2
        r = GenerateSizeList(ReSizeList)
        for i in range(len(r)):
            Q = Exponentiate(P, ReSizeList[i])
            FactorList[i] = execute(Q/c_int, Q*c_int)
            F *= FactorList[i]
            
        I1 = (P1 - 1)/ 2*F
        I2 = (P2 - 1) / 2*F
        success = False
        while True:
            R = random.randint(I1, I2)
            n = 2*F*R + 1
            if TrialDivision(n):
                a = random.randint(2, n-1)
                success = Checklemma1(n, a, FactorList) 
            if success:
                break
        return n


def getArr(n):
    

    isprime = [True for _ in range(n)]  
    prime = []  
    spf = [None for _ in range(n)]
        
    isprime[0] = isprime[1] = False
    for i in range(2, n):
        if isprime[i]:
            prime.append(i)
            spf[i] = i
                
        j = 0
        while (j < len(prime) and i * prime[j] < n and prime[j] <= spf[i]):
            isprime[i * prime[j]] = False
            spf[i * prime[j]] = prime[j] 
                
            j += 1

    return prime


def is_probably_prime(n, sieve):
    for x in sieve:
        if n % x == 0:
            return False
    return True


def generatePrime(n : int, primes = None, s = None):
    
    up_limit = 10**n


    if not primes: 
        primes = getArr(1000)

    if not s: s = primes[-1] 
    while s < up_limit:
        lo, l1 = (s + 1) >> 1, (s << 1) + 1

        while True:
            r = random.randint(lo, l1) << 1 
            n = s*r + 1 
            if not is_probably_prime(n, primes): continue
            while True:
                a = random.randint(2, n-1)
                if pow(a, n-1, n) != 1: break

                d = math.gcd((pow(a, r, n) - 1) % n, n)
                if d != n:
                    if d == 1: s = n 
                    else: 
                        pass 
                    break
                else: 
                    pass 
            if s == n: break
    return s



def main():
    from functions import Luke
    import time 
    start = time.time()
    state = True
    luke = Luke()
    
    for i in range(1000):
        if not state:
            break
        
        prime = generatePrime(4) 
        if not luke.LucasMethod(prime):
            state = False
        print(prime)
    
    print(state)
    end = time.time()
    print(f" Resulting time was = {end - start} sec.")
    
    
if __name__ == "__main__":
    main()