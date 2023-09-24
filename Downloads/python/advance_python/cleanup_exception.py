try:
    # Code that may raise an exception
    file = open("example.txt", "r")
    data = file.read()
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print('Creating the file')
    file=open("example.txt", "w")
finally:
    # Clean-up action: close the file
    if 'file' in locals():
        file.close()
    print("File closed")