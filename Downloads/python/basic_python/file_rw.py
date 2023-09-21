# Creating a file and writing to it
f_name=input('Enter file name of your choice with extension (.txt) : ')
try:
    # Open a file for writing (mode 'w' creates a new file or truncates an existing one)
    with open(f_name, 'w') as file:
        while True:
                line = input("Enter a line of text (or 'exit' to quit): ")
                if line.lower() == 'exit':
                    break
                else:
                    # Write the user's input to the file
                    file.write(line + '\n')

        print(f"Data has been written to {f_name} successfully!")
        
except IOError as e:
    print(f"An error occurred: {e}")

# Reading from a file
print(f"\n The content in the {f_name} is \n")
try:
    # Open a file for reading (mode 'r' opens an existing file for reading)
    with open(f_name, 'r') as file:
        contents = file.read()
        print(contents)

except IOError as e:
    print(f"An error occurred: {e}")
