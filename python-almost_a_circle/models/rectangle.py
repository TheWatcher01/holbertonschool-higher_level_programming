#!/usr/bin/python3
""" Module for Rectangle class. """
from models.base import Base


class Rectangle(Base):
    """ Rectangle class that inherits from Base. """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialize a new Rectangle. """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get/set width of Rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Get/set height of Rectangle. """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Get/set x coordinate of Rectangle. """
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Get/set y coordinate of Rectangle. """
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns area value of Rectangle instance."""
        return self.width * self.height

    def display(self):
        """
        Prints in stdout Rectangle instance with character '#'.
        """
        print("\n" * self.y, end="")
        for row in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Overrides str method to return Rectangle instance
        representation.
        """
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute or key/value
        argument to attributes.
        """
        attributes = [
            "id", "width", "height", "x", "y"
        ]
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns dictionary representation of a Rectangle."""
        return {
            'id': self.id, 'width': self.width,
            'height': self.height, 'x': self.x, 'y': self.y
        }
