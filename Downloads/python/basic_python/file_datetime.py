import os
import datetime

def get_file_creation_time(path):
    try:
        # Get file creation time (Windows) or metadata change time (Unix)
        if os.name == 'nt':  # Windows
            return datetime.datetime.fromtimestamp(os.path.getctime(path))
        else:  # Unix
            stat = os.stat(path)
            try:
                return datetime.datetime.fromtimestamp(stat.st_birthtime)
            except AttributeError:
                return datetime.datetime.fromtimestamp(stat.st_mtime)
    except FileNotFoundError:
        return None

def get_file_modification_time(path):
    try:
        # Get file modification time
        stat = os.stat(path)
        return datetime.datetime.fromtimestamp(stat.st_mtime)
    except FileNotFoundError:
        return None

def main():
    file_path = input("Enter the file path: ")
    
    creation_time = get_file_creation_time(file_path)
    if creation_time:
        print(f"File creation time: {creation_time}")
    else:
        print("File creation time not available.")

    modification_time = get_file_modification_time(file_path)
    if modification_time:
        print(f"File modification time: {modification_time}")
    else:
        print("File modification time not available.")

if __name__ == "__main__":
    main()
