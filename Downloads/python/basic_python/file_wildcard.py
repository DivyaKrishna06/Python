import glob

def find_files_with_wildcard(pattern):
    """
    Find files that match the specified wildcard pattern.
    
    Args:
        pattern (str): The wildcard pattern to search for.
        
    Returns:
        list: A list of file paths that match the pattern.
    """
    matching_files = glob.glob(pattern)
    return matching_files

if __name__ == "__main__":
    wildcard_pattern = input("Enter a wildcard pattern (e.g., '*.txt'): ")
    
    matching_files = find_files_with_wildcard(wildcard_pattern)
    
    if matching_files:
        print("Matching files:")
        for file_path in matching_files:
            print(file_path)
    else:
        print("No matching files found.")