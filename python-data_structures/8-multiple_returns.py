#!/usr/bin/python3

"""
def multiple_returns(sentence):

Description:

'multiple_returns' function takes a sentence as an argument.
It returns a tuple with length of sentence and its first character.
If the sentence is empty, it returns 0 and None.

Arguments:
"sentence" - string to analyze

Return:
Function returns a tuple with length of sentence and its first character,
or (0, None) if the sentence is empty.
"""


def multiple_returns(sentence):
    # Define function 'multiple_returns' with one parameter: 'sentence'.

    if sentence:
        # If 'sentence' is not empty
        return (len(sentence), sentence[0])
        # return a tuple with length of 'sentence' and its first character.

    else:
        # If 'sentence' is empty
        return (0, None)
        # return a tuple with 0 and None.
