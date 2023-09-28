# Extended actual argument syntax
t = (1, 2, 3, 4, 5)

def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)

# Unpack the first two elements of the tuple into arg1 and arg2, and the rest go to args
print_args(*t)