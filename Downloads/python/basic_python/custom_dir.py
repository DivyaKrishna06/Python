def custom_dir(obj=None):
    if obj is None:
        # If no argument is provided, list the current scope's names
        return [name for name in globals() if not name.startswith("__")]
    else:
        # List the attributes and methods of the provided object
        return [name for name in dir(obj) if not name.startswith("__")]

# Example usage:
if __name__ == "__main__":
    # List the attributes and methods of the 'str' class
    print("Attributes and methods of 'str' class:")
    print(custom_dir(str))

    # List the attributes and methods of a custom object
    class CustomObject:
        def __init__(self):
            self.attribute1 = 1
            self.attribute2 = "Hello"
        
        def method(self):
            pass

    custom_instance = CustomObject()
    print("\nAttributes and methods of 'custom_instance':")
    print(custom_dir(custom_instance))

    # List the names in the current scope
    print("\nNames in the current scope:")
    print(custom_dir())