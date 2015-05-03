import math
class Ellipse:
    def Ellipse(self,x,y):
        return(math.pi*x*y)
class Square:
    def Square(self,z):
        return(z*z)
class Rectangle:
    def Rectangle(self,m,n):
        return m*n
class Circle:
    def Circle(self,f):
        return math.pi*f*f
class Myclass(Ellipse,Square,Rectangle,Circle):
    def compute_area(self,shapes):
        for i in range(0,len(shapes)):
            print(shapes[i])
        return(sum(shapes))
q=Myclass()
print("总面积是：",q.compute_area([q.Ellipse(20,35),q.Square(15),q.Rectangle(13,20)]))
