import math
import random

class Maurer():
    c_int = 1.2
    rmax = 10
    P0 = math.pow(10,20)
    P = 0
    FactorList = [0] * rmax
    SizeList = [0.0] * rmax
    
    def Sqrt(self,a):
        return int(math.sqrt(a))
    
    def Exp(self,a, e):
        return int(a ** e)

    def IsPrime(self,a):
        if a < 2:
            return False
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True


    def     IsTrivialDivision(self,a):
        if a < 2:
            return False
        for i in range(2, int(math.sqrt(a)) + 1):
            if a % i == 0:
                return False
        return True

  
    def GenSizeList(self,SList):
        c = 1
        while True:
            u = random.uniform(0, c)
            SList.append(u)
            c = c - u
            SList.sort(reverse=True)
            for i in range(len(SList)):
                if SList[i] > 1 - sum(SList[0:i+1]):
                    return SList[0:i+1]
   
   
    def IsLemma(self,n,a ,flist):
        if (math.pow(a, n-1)) % n != 1:
            return False
        for i in flist:
            if math.gcd(a**((n-1)//i) - 1, n) != 1:
                return False
        return True


    def execute(self,P1, P2):
        if P2 <= self.P0:
            while True:
                n = random.randint(P1, P2)
                if self.IsPrime(n):
                    break
            return n
        else:
            F = 1
            p = (self.Sqrt((P1 - 1) * (P2 - 1))) / 2
            r = self.GenSizeList(self.SizeList)
            for i in range(len(r)):
                Q = self.Exp(self.P, self.SizeList[i])
                self.FactorList[i] = self.execute(Q/self.c_int, Q*self.c_int)
                F *= self.FactorList[i]
                
            I1 = (P1 - 1)/ 2*F
            I2 = (P2 - 1) / 2*F
            success = False
            while True:
                R = random.randint(I1, I2)
                n = 2*F*R + 1
                if self.IsTrivialDivision(n):
                    a = random.randint(2, n-1)
                    success = self.IsLemma(n, a, self.FactorList) 
                if success:
                    break
            return n



class Luke():

    def divisions(self,n, divisions): # i don't know how the word "разложение"
                                # ought to be in english let if be "division"
                                # what asically means the numbers that can be divided into
        import math
        
        if (n % 2 == 0):
            divisions.append(2)
            
        while (n % 2 == 0):
            n = n // 2            
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if (n % i == 0):
                divisions.append(i)
                
            while (n % i == 0):
                n = n // i
                
        if (n > 2):
            divisions.append(n)
            
        return divisions    


    def pow(self,n, r, q):
        res = n
        for i in range(1, r):
            res = (res * n) % q
        return res
    

    def LucasMethod(self,x, seed = 76619464691):
        import random
        random.seed(seed)   
        
        factors = []
        factors = self.divisions(x - 1, factors)

        # array for randomly selecting x-1 numbers
        rand = [i for i in range(x - 1)]          
        # randomly shuffle all the numbers in array
        random.shuffle(rand)

        for i in range(x - 1):
            a = rand[i] 
            # If a^(n-1) not equal 1 
            if (self.pow(a, x- 1, x) != 1):
                return False
            
            flag = True
            for k in range(len(factors)):  
                # If a^((n-1)/q) equal 1
                if (self.pow(a, (x - 1) // factors[k], x) == 1):
                    flag = False
                    break
    
            if (flag):
                return True
        
        return False