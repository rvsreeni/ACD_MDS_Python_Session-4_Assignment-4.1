# Assignment 4.1
class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        
    def __str__(self):
        return "Triangle has 3 sides %d, %d, %d ." % (self.side1, self.side2, self.side3)

class Calculate(Triangle):
    def __init__(self, *args, **kwargs):
        super(Calculate, self).__init__(*args, **kwargs)
        
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return ((s*(s - self.side1)*(s - self.side2)*(s - self.side3)) ** 0.5)
 
tri1 = Triangle(6, 8, 10)
print(tri1)
calc1 = Calculate(6, 8, 10)   
print("Area of triangle is %d " % calc1.area())       
        
        
def filter_long_words(wdlist,n):
    outlist = []
    for wd in wdlist:
        if (len(wd) > n):
            outlist.append(wd)
    return outlist

input_list = ['one','two','three','four']
print(filter_long_words(input_list, 3))

        
        