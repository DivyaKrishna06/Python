def convert_upper(f):
    print("convert_upper")
    def wrap(*args, **kwargs):
        print("wrap")
        x = f(*args, **kwargs)
        return x.upper()
    return wrap

@convert_upper
def my_name(name):
    print("my_name")
    return name

name=input('Enter name in lower case:')
result=my_name(name)
print("Name is ", result)