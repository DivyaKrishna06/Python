def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Reading from {file_name}:\n{content}")
    except FileNotFoundError:
        print(f"{file_name} not found.")

def write_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)
        print(f"Writing to {file_name}:\n{content}")

def execute_file(file_name):
    try:
        exec(open(file_name).read())
        print(f"Executing {file_name}")
    except FileNotFoundError:
        print(f"{file_name} not found.")
    except Exception as e:
        print(f"Error executing {file_name}: {str(e)}")

def append_file(file_name, content):
    with open(file_name, 'a') as file:
        file.write(content)
        print(f"Appending to {file_name}:\n{content}")

def open_file(file_name, mode):
    try:
        file = open(file_name, mode)
        print(f"Opened {file_name} in mode: {mode}")
        return file
    except FileNotFoundError:
        print(f"{file_name} not found.")
        return None

def close_file(file):
    if file:
        file.close()
        print(f"Closed file.")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Read file")
        print("2. Write to file")
        print("3. Execute file")
        print("4. Append to file")
        print("5. Open file")
        print("6. Close file")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_name = input("Enter the file name to read: ")
            read_file(file_name)
        elif choice == '2':
            file_name = input("Enter the file name to write to: ")
            content = input("Enter content to write: ")
            write_file(file_name, content)
        elif choice == '3':
            file_name = input("Enter the file name to execute: ")
            execute_file(file_name)
        elif choice == '4':
            file_name = input("Enter the file name to append to: ")
            content = input("Enter content to append: ")
            append_file(file_name, content)
        elif choice == '5':
            file_name = input("Enter the file name to open: ")
            mode = input("Enter file mode (e.g., 'r', 'w', 'a'): ")
            file = open_file(file_name, mode)
        elif choice == '6':
            if 'file' in locals():
                close_file(file)
            else:
                print("No file is currently open.")
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please try again.")