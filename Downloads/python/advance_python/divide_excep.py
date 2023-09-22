def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

n1=int(input('Enter the dividend: '))
n2=int(input('Enter the divisor: '))
divide(n1,n2)