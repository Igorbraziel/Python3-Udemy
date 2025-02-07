def soma(x, y):
    """Soma X e Y
    
    >>> soma(10, 20)
    30
    
    >>> soma('10', 20)
    Traceback (most recent call last):
    ...
    AssertionError: X must be int or float
    """
    assert isinstance(x, (int, float)), 'X must be int or float'
    assert isinstance(y, (int, float)), 'Y must be int or float'
    return x + y

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)