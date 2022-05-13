import math

class Point2D():
    
    def __init__(self,x:float,y:float) -> None:
        self.x = x
        self.y = y

    # this is a method
    def modulus(self)->float:
        return math.sqrt( self.x**2 + self.y**2 )

if __name__=="__main__":
    print(type(Point2D.modulus))
    p1 = Point2D(3,2)
    print(type(p1.modulus))
    print(p1.modulus())
    print(Point2D.modulus(p1))