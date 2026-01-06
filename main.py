class Kalkulator:
    def __init__(self, i,j):
        self.i = i
        self.j = j
        
        
    def plus(self):
        return self.i + self.j
    
    def min(self):
          return self.i - self.j
        
        
    def times(self):
            return self.i * self.j
        
        
    def divided(self):
        if self.j == 0 :
            return " 0 is not definited"
        
number = Kalkulator(9,110)
print(number.plus())
print(number.divided())
print(number.min())
print(number.times())

      
      