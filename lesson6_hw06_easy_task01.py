from math import sqrt

class triangle:
    def __init__(self, c1_x, c1_y, c2_x, c2_y, c3_x, c3_y):
        self.c1_x = c1_x
        self.c1_y = c1_y
        self.c2_x = c2_x
        self.c2_y = c2_y
        self.c3_x = c3_x
        self.c3_y = c3_y
        self.c1_c2 = sqrt(int((c1_x - c2_x)**2 + (c1_y - c2_y)**2))
        self.c2_c3 = sqrt(int((c2_x - c3_x)**2 + (c2_y - c3_y)**2))
        self.c3_c1 = sqrt(int((c3_x - c1_x)**2 + (c3_y - c1_y)**2))

    def perimetr(self):
        self.perimetr = self.c1_c2 + self.c2_c3 + self.c3_c1
        return (self.perimetr)

    def square(self):
        self.perimetr /= 2
        self.square = sqrt(self.perimetr*(self.perimetr - self.c1_c2)*(self.perimetr - self.c2_c3)*(self.perimetr - self.c3_c1))
        return (self.square)

    def height(self):
        self.square *= 2
        self.height = self.square / self.c1_c2





