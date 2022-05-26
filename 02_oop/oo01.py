import math

class Vec2D():
    
    def __init__(self,x:float,y:float) -> None:
        self.x = x
        self.y = y

    # this is a method
    def length(self)->float:
        return math.sqrt( self.x**2 + self.y**2 )

if __name__=="__main__":
    print(type(Vec2D.length))
    p1 = Vec2D(3,2)
    print(type(p1.length))
    print(p1.length())
    print(Vec2D.length(p1))