class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.init_singleton()
        return cls._instance

    def init_singleton(self):
        # This method can be used to initialize instance-specific attributes.
        pass

# Usage
if __name__ == "__main__":
    s1 = Singleton()
    s1.some_attribute = "Hello, I'm the first instance."

    s2 = Singleton()

    # Both s1 and s2 will refer to the same instance
    print(s1 is s2)  # True
    print(s2.some_attribute)  # "Hello, I'm the first instance."