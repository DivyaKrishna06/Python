class MyContextManager:
    def __enter__(self):
        # Code to run before entering the context
        print("Entering the context")
    
    def __exit__(self, exc_type, exc_value, traceback):
        # Code to run after exiting the context
        print("Exiting the context")

# Using the context manager
with MyContextManager():
    print("Inside the context")