import contextlib

@contextlib.contextmanager
def propagater(name, propagate):
    try:
        yield
        print(name, 'exited normally.')
    except Exception:
        print(name, 'received an exception!')
        if propagate:
            raise

# Example usage of the propagater context manager
if __name__ == "__main__":
    with propagater("Context A", propagate=True):
        print("Inside Context A")
        # Simulate an exception
        raise ValueError("An error occurred in Context A")

    with propagater("Context B", propagate=False):
        print("Inside Context B")
        # Simulate an exception
        raise ValueError("An error occurred in Context B")