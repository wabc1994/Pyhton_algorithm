

def all(iterable):
    """
    return true if all elements of the iterable are true
     (or if the iterable is empty)
    :param iterable:
    :return:
    """
    for element in iterable:
        if not element:
            return False
    return True

def any(iterable):
    """

    :param iterable:
    :return:
    """
    for element in iterable:
        if element:
            return True
    return False


