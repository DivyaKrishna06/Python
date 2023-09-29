# Define a generator function that generates numbers from 0 to n-1
def custom_iterator(n):
    for i in range(n):
        yield i

# Create an iterator using the generator function
iterator = custom_iterator(5)

print('Generator:')
# Iterate through the custom iterator
for num in iterator:
    print(num)

# Define a custom iterator class
class CustomIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.n:
            result = self.current
            self.current += 1
            return result
        else:
            raise StopIteration

# Create an iterator using the custom iterator class
iterator = CustomIterator(5)

print('Iterator class:')
# Iterate through the custom iterator
for num in iterator:
    print(num)