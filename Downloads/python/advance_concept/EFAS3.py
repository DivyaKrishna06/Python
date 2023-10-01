# Extended argument syntax
def func(arg1, arg2, *args, kwarg1, **kwargs):
    print("Type of arg1:", type(arg1))
    print("Value of arg1:", arg1)
    
    print("Type of arg2:", type(arg2))
    print("Value of arg2:", arg2)
    
    print("Type of args:", type(args))
    print("Value of args:", args)
    
    print("Type of kwarg1:", type(kwarg1))
    print("Value of kwarg1:", kwarg1)
    
    print("Type of kwargs:", type(kwargs))
    print("Value of kwargs:", kwargs)

func(1, 2, 3, 4, 5, kwarg1="Hello", kwarg2="World")