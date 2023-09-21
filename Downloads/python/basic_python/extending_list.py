class ExtendingList(list):
    def extend(self, iterable):
        """
        Extend the list by appending elements from the iterable.
        
        Args:
            iterable (iterable): An iterable containing elements to be added to the list.
        """
        for item in iterable:
            self.append(item)

    def remove_all(self, value):
        """
        Remove all occurrences of a specific value from the list.

        Args:
            value: The value to be removed.
        """
        while value in self:
            self.remove(value)

    def unique(self):
        """
        Remove duplicate elements from the list, preserving the order.
        """
        seen = set()
        unique_list = []
        for item in self:
            if item not in seen:
                seen.add(item)
                unique_list.append(item)
        return unique_list

# Example usage:
my_list = ExtendingList([1, 2, 3])
my_list.extend([4, 5, 6])
print(my_list)  # Output: [1, 2, 3, 4, 5, 6]

my_list.remove_all(2)
print(my_list)  # Output: [1, 3, 4, 5, 6]

my_list.extend([4, 5, 6])
unique_list = my_list.unique()
print(unique_list)  # Output: [1, 3, 4, 5, 6]
