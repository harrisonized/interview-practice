# Functions
# # get_digit
# # digits_num_to_tuple
# # digits_tuple_to_num
# # digitize


def get_digit(number, n):
    """ see: https://stackoverflow.com/questions/39644638/how-to-take-the-nth-digit-of-a-number-in-python
    """
    return number // 10**n % 10


def digits_num_to_tuple(num, num_digits):
    """Example:
    digits_num_to_tuple(203, 3)
    (3, 0, 2)
    """
    return tuple([get_digit(num, digit) for digit in list(range(num_digits))])


def digits_tuple_to_num(digits: tuple):
    """Example:
    digits_tuple_to_num((3, 0, 2))
    203
    """
    
    num = 0
    for i, digit in enumerate(digits):
        num += digit*(10**i)
        
    return num


def digitize(n, base=10):
    """Alternative to digits_num_to_tuple
    see: https://stackoverflow.com/questions/1906717/splitting-integer-in-python
    Eg. tuple(digitize(203))
    (2, 0, 3)
    """
    if n == 0:
        yield 0
    while n:
        n, d = divmod(n, base)
        yield d
