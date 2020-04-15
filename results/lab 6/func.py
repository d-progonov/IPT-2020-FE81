class Rational():
    def __init__(self, numerator=0, demoniator=1):
        self.numer = numerator
        self.denom = demoniator

    def __add__(self,other):
        n1 = self.numer
        d1 = self.denom
        n2 = other.numer
        d2 = other.denom
        n3 = d2*n1 + d1*n2 
        d3 = d1*d2
        return Rational(n3,d3)
    
    def __mul__(self, other):
        n1 = self.numer
        d1 = self.denom
        n2 = other.numer
        d2 = other.denom
        n3 = n1*n2 
        d3 = d1*d2
        return Rational(n3,d3)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)

    def reduce(self):
        d = 1
        if self.denom != 0 and self.numer != 0:
            d = self.gcd(self.numer, self.denom)

        if d > 1:
            self.numer /= d
            self.denom /= d
            a = Rational(int(self.numer),int(self.denom))
            return a
    
    def __str__(self):
        return "{0}/{1}".format(self.numer,self.denom)