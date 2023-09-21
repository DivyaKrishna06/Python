import os

def main():
    while True:
        print("\nSelect an option:")
        print("1. List files in the current directory")
        print("2. Create a new directory")
        print("3. Run a command")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            list_files()
        elif choice == "2":
            create_directory()
        elif choice == "3":
            run_command()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def list_files():
    files = os.listdir()
    print("\nFiles in the current directory:")
    for file in files:
        print(file)

def create_directory():
    directory_name = input("\nEnter the directory name: ")
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except Exception as e:
        print(f"Error creating directory: {str(e)}")

def run_command():
    command = input("\nEnter the command to run: ")
    try:
        result = os.system(command)
        if result == 0:
            print(f"Command '{command}' executed successfully.")
        else:
            print(f"Command '{command}' returned a non-zero exit code.")
    except Exception as e:
        print(f"Error running command: {str(e)}")

if __name__ == "__main__":
    main()