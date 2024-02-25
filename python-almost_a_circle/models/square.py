#!/usr/bin/python3
""" Module for Square class. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square class inheriting from Rectangle. """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize a new Square instance. """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Size of the Square. """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """ String representation of the Square. """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - " +
                f"{self.width}")

    def update(self, *args, **kwargs):
        """ Update Square attributes. """
        attrs = ["id", "size", "x", "y"]
        if args:
            for attr, value in zip(attrs, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """ Dictionary representation of the Square. """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
