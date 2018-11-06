from math import sqrt

class Равнобочная_трапеция:
    def __init__(self, c1_x, c1_y, c2_x, c2_y, c3_x, c3_y, c4_x, c4_y):
        self.c1_x = c1_x
        self.c1_y = c1_y
        self.c2_x = c2_x
        self.c2_y = c2_y
        self.c3_x = c3_x
        self.c3_y = c3_y
        self.c4_x = c4_x
        self.c4_y = c4_y

    def sides(self):
        self.c1_c2 = sqrt(int((c1_x - c2_x)**2 + (c1_y - c2_y)**2))
        self.c2_c3 = sqrt(int((c2_x - c3_x)**2 + (c2_y - c3_y)**2))
        self.c3_c4 = sqrt(int((c3_x - c4_x)**2 + (c3_y - c4_y)**2))
        self.c4_c1 = sqrt(int((c4_x - c1_x)**2 + (c4_y - c1_y)**2))

    def check(self):
        if self.c1_c2 == self.c3_c4 or self.c2_c3 == self.c4_c1:
            print("This trapeze is isosceles")
        else:
            print("This trapeze is not isosceles")

    def perimetr(self):
        self.perimetr = self.c1_c2 + self.c2_c3 + self.c3_c4 + self.c4_c1
        return (self.perimetr)

    def square(self):
        if self.c1_c2 == self.c3_c4 and self.c2_c3 > self.c4_c1:
            self.square = ((self.c2_c3 + self.c4_c1) / 2) * sqrt(self.c1_c2**2 - ((self.c2_c3 - self.c4_c1)**2) / 4)
        elif self.c1_c2 == self.c3_c4 and self.c2_c3 < self.c4_c1:
            self.square = ((self.c2_c3 + self.c4_c1) / 2) * sqrt(self.c1_c2**2 - ((self.c4_c1 - self.c2_c3)**2) / 4)
        elif self.c2_c3 == self.c4_c1 and self.c1_c2 > self.c3_c4:
            self.square = ((self.c2_c3 + self.c4_c1) / 2) * sqrt(self.c2_c3**2 - ((self.c1_c2 - self.c3_c4)**2) / 4)
        elif self.c2_c3 == self.c4_c1 and self.c1_c2 < self.c3_c4:
            self.square = ((self.c2_c3 + self.c4_c1) / 2) * sqrt(self.c2_c3**2 - ((self.c3_c4 - self.c1_c2)**2) / 4)
        return (self.square)




