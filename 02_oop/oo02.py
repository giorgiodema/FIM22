from __future__ import annotations
import math

class Vec2D():

    def __init__(self,x:float,y:float):
        self.x = x
        self.y = y
   
    def length(self) -> float:
        return math.sqrt( self.x**2 + self.y**2 )

    def __add__(self, v:Vec2D) -> Vec2D:
        return Vec2D(self.x + v.x, self.y + v.y)

    def __str__(self) -> str:
        return "Vec.x = {}, Vec.y = {}".format(self.x,self.y)


v1 = Vec2D(2,3)
v2 = Vec2D(3,5)

v3 = v1 + v2

print(v3)

