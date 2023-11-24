class rectrangle:
    def __init__(self, length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length + self.width)

lengthinput = int(input("Enter the length of the Rectrangle"))
widthinput = int(input("Enter the width of the rectrangle"))

values= rectrangle(lengthinput,widthinput)

print(f"Area of Rectrangle: {values.area()}")
print(f"Perimeter of Rectrangle : {values.perimeter()}")