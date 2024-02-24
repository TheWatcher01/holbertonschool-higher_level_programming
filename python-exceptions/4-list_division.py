#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
    Divide elements of two lists, handle errors.

    Function tries to divide elements of two lists.
    If error occurs (zero division, wrong type, index out of range),
    it prints error message and uses 0 as division result.

    Args:
        my_list_1: First list of numbers.
        my_list_2: Second list of numbers.
        list_length: Length of lists.

    Returns:
        list: List containing results of division.
    """
    # Initialize list of zeros of specified length
    result = [0] * list_length

    # Iterate over indices from 0 to list_length - 1
    for i in range(list_length):
        try:
            # Try to divide elements of two lists
            result[i] = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            # Handle case where second number is zero
            print("division by 0")
        except TypeError:
            # Handle case where one of elements is not number
            print("wrong type")
        except IndexError:
            # Handle case where one of indices is out of lists' bounds
            print("out of range")
        finally:
            # Ensure result[i] is defined even if an exception is raised
            if type(result[i]) is not float:
                result[i] = 0

    # Return list of results
    return result
