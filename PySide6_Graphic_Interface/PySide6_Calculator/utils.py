import re

NUM_OR_DOT_REGEX = re.compile(r'^[0-9.]$')

def isNumOrDot(string: str) -> bool:
    return bool(NUM_OR_DOT_REGEX.search(string))

def isValidNumber(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False   
    
def isEmpty(string: str) -> bool:
    return len(string) == 0 

