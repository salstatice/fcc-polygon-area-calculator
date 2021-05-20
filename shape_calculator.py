class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height =  height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        if self.width and self.height:
            return self.width * self.height

    def get_perimeter(self):
        if self.width and self.height:
            return self.width * 2 + self.height * 2

    def get_diagonal(self):
        if self.width and self.height:
            return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        if self.width and self.height:
            if self.width > 50 or self.height > 50:
                return "Too big for picture."
            else:
                temp = ['*' * self.width + '\n' for i in range(self.height)]
                return ''.join(temp)
    
    def get_amount_inside(self, inside_shape):
        if isinstance(inside_shape, Square):
            col = self.width // inside_shape.width
            row = self.height // inside_shape.height
            return col * row
        else:
            possibility = []
            # layout-1
            col_1 = self.width // inside_shape.width
            row_1 = self.height // inside_shape.height
            possibility.append(col_1 * row_1)
            if self.width % inside_shape.width > inside_shape.height:
                sub_section = Rectangle(self.width % inside_shape.width, self.height)
                extra = sub_section.get_amount_inside(inside_shape)
                possibility.append(col_1 * row_1 + extra)
            elif self.height % inside_shape.height > inside_shape.width:
                sub_section = Rectangle(self.height % inside_shape.height, self.width)
                extra = sub_section.get_amount_inside(inside_shape)
                possibility.append(col_1 * row_1 + extra)
                
            # layout-2
            col_2 = self.width // inside_shape.width
            row_2 = self.height // inside_shape.height
            if self.width % inside_shape.width > inside_shape.height:
                sub_section = Rectangle(self.width % inside_shape.width, self.height)
                extra = sub_section.get_amount_inside(inside_shape)
                possibility.append(col_2 * row_2 + extra)
            elif self.height % inside_shape.height > inside_shape.width:
                sub_section = Rectangle(self.height % inside_shape.height, self.width)
                extra = sub_section.get_amount_inside(inside_shape)
                possibility.append(col_2 * row_2 + extra)
            possibility.append(col_2 * row_2)

            return max(possibility)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.width = height
        self.height = height

    def __str__(self):
        return "Square(side={})".format(self.width)