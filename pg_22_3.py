try:
    import math
    # Math.pow(5, 2)
except (ZeroDivisionError, TypeError, ValueError):
    print('Exception Encountered')
except:
    print('This might be a NameError')

# NameError - Wrong Syntax / Undeclared Variable
# TypeError - When a variable is not defined
# ZeroDivisionError - When a number is divided by 0
# ValueError - When type conversion is not possible
