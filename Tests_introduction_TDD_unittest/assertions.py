def soma(x, y):
    assert isinstance(x, (int, float)), 'X must be int or float'
    assert isinstance(y, (int, float)), 'Y must be int or float'
    return x + y

try:
    print(soma(15, '15'))
except AssertionError as assertion_error:
    print(assertion_error)
    
print(soma(15, 15))
    