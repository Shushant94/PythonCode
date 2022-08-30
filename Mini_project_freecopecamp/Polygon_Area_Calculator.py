#Classe Padre
class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height= height

    def set_width(self,wd):
        self.width = wd
    def set_height(self,hg):
        self.height = hg
    def get_area(self):
        Area = (self.width * self.height)
        return Area

    def get_perimeter(self):
        perimeter = (2 * self.width + 2 * self.height)
        return perimeter
    def get_diagonal(self):
        print(self.width)
        print(self.height)
        diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
        return diagonal
    #Drawing the star
    def get_picture(self):
        picture = ""
        Star = "*"
        row= self.height
        colum = self.width
        if self.width <= 50 or self.height <=50:
            for row_star in range(0,row):
                for colum_star in range(0,colum):
                    picture = picture+Star
                picture = picture +"\n"
        else:
            picture = "Too big for picture"
        return picture
    def get_amount_inside(self,sq):
        result = 0
        area_sq = sq.width * sq.height
        area_rect = self.width * self.height
        result = area_rect / area_sq
        return int(result)
    def __str__(self):
        strg = "Rectangle(width={},height={})".format(self.width,self.height)
        return strg
#Classe hijo
class Square(Rectangle):
    def __init__(self,side):
        self.side = side
        self.set_width(side)
        self.set_height(side)

    def set_side(self,side):
        self.side = side
        self.set_width(side)
        self.set_height(side)
        return self.side
    def __str__(self):
        strg = "Square(side={})".format(self.side)
        return strg

#Rectangle
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

#Square
sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

#How many square can we add in rectange
rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))