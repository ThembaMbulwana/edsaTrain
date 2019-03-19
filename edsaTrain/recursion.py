def sum_array(array):
    """ Return sum of all items in array recursively """
    return array[0] + sum_array(array[1:]) if array else 0

def fibonacci(n):
    """ Ruturn nth term in fibonacci sequence """
    return n if n <= 1 else fibonacci(n - 1) + fibonacci(n -2)

def factorial(n):
    """ Return n! """
    return 1 if n < 1 else n * factorial(n -1)

def  reverse(word):
    """ Return word in reverse """
    return word[-1] + reverse(word[:-1]) if len(word) > 1 else word