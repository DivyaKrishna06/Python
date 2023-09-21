import os

def get_file_size(file_path):
    try:
        # Get the size of the file in bytes
        size = os.path.getsize(file_path)
        return size
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    file_path = input("Enter the path of the file: ")
    file_size = get_file_size(file_path)
    
    if isinstance(file_size, int):
        print(f"The size of the file '{file_path}' is {file_size} bytes.")
    else:
        print(file_size)
