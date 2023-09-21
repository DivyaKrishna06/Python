def sort_dictionary(d, by_key=True):
    if by_key:
        sorted_dict = dict(sorted(d.items()))
    else:
        sorted_dict = dict(sorted(d.items(), key=lambda item: item[1]))
    return sorted_dict

def main():
    user_dict = {}
    while True:
        key = input("Enter a key (or 'done' to finish): ")
        if key.lower() == 'done':
            break
        value = input("Enter a value: ")
        user_dict[key] = value

    print("Original Dictionary:")
    for key, value in user_dict.items():
        print(f"{key}: {value}")

    while True:
        sort_option = input("Sort by (k)ey or (v)alue, or (q)uit: ").lower()
        if sort_option == 'k':
            sorted_dict = sort_dictionary(user_dict, by_key=True)
            break
        elif sort_option == 'v':
            sorted_dict = sort_dictionary(user_dict, by_key=False)
            break
        elif sort_option == 'q':
            return
        else:
            print("Invalid option. Please enter 'k' for key sorting, 'v' for value sorting, or 'q' to quit.")

    print("Sorted Dictionary:")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
