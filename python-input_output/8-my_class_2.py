#!/usr/bin/python3
"""
Module defines MyClass class, which is simple demonstration of class
with methods for winning and losing in game.
"""


class MyClass:
    """
    A simple class to represent a game participant.

    Attributes:
        score (int): Score of game participant, initialized to 0.
    """

    score = 0  # Static class variable to track the score

    def __init__(self, name, number=4):
        """
        The constructor for MyClass.

        Args:
            name (str): The name of the game participant.
            number (int, optional): Identifier number for participant.
            Defaults to 4.

        Constructor also initializes boolean attribute `is_team_red`
        to determine team based on number.
        """
        # Private variable for participant's name
        self.__name = name
        # Public variable for participant's identifier number
        self.number = number
        # Determine team color based on 'number'
        self.is_team_red = (self.number % 2) == 0

    def win(self):
        """
        Increments the score by 1 to signify a win.
        """
        self.score += 1

    def lose(self):
        """
        Decrements the score by 1 to signify a loss.
        """
        self.score -= 1

    def __str__(self):
        """
        String representation of the MyClass instance.

        Returns:
            str: Formatted string representing MyClass instance,
            including name, number, and score.
        """
        return "[MyClass] {} - {:d} => {:d}".format(self.__name, self.number, self.score)
