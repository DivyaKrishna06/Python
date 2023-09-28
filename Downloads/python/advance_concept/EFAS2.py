def extended_args_example(*args, **kwargs):
    print("Positional arguments:")
    for arg in args:
        print(arg)

    print("\nKeyword arguments:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Example usage
extended_args_example(1, 2, 3, name="John", age=30, city="New York")