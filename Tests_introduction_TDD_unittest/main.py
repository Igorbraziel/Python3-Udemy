from calculator import soma

try:
    print(soma(15, '15'))
except AssertionError as assertion_error:
    print(assertion_error)
    
print(soma(15, 15))
    