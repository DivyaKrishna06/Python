def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return f"File '{file_name}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def write_file(file_name, content):
    try:
        with open(file_name, 'w') as file:
            file.write(content)
        return f"Successfully wrote to '{file_name}'."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def execute_file(file_name):
    try:
        exec(open(file_name).read())
        return f"Successfully executed '{file_name}'."
    except FileNotFoundError:
        return f"File '{file_name}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"

def append_file(file_name, content):
    try:
        with open(file_name, 'a') as file:
            file.write(content)
        return f"Successfully appended to '{file_name}'."
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    file_name = "sample.txt"

    # Read from a file
    content = read_file(file_name)
    print("Content of the file:")
    print(content)

    # Write to a file
    write_content = "This is a new content to write to the file."
    write_result = write_file(file_name, write_content)
    print(write_result)

    # Execute a file (if it's a Python script)
    execute_result = execute_file("sample_script.py")
    print(execute_result)

    # Append to a file
    append_content = "\nThis is appended content."
    append_result = append_file(file_name, append_content)
    print(append_result)