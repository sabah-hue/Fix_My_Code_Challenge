#!/usr/bin/python3
"""square class"""


class Square():
    """Class Square"""
    width = 0
    height = 0

    def __init__(self, width, height):
        """init class"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """PermiterOfMySquare"""
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """return string"""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """test my classe"""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
