import math

class Point2D():

    npoints = 0
    
    def __init__(self,x:float,y:float) -> None:
        self.x = x
        self.y = y
        Point2D.npoints += 1

    # this is a method
    def modulus(self)->float:
        return math.sqrt( self.x**2 + self.y**2 )

if __name__=="__main__":
    
    print(Point2D.npoints)

    p1 = Point2D(1.,3.)
    p2 = Point2D(3.,4.)

    print(Point2D.npoints)
    
    print(p2.npoints)

    print(p1.modulus())
    print(p2.modulus())