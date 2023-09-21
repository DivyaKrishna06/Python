#generator function - A generator function is defined using the yield keyword. 
#When a function contains one or more yield statements, it becomes a generator function

def number_generator(n):
    for i in range(n):
        yield i

# Using the generator
gen = number_generator(5)
for num in gen:
    print(num)


#A generator expression is a concise way to create a generator. 
#It's similar to a list comprehension, but it uses parentheses instead of square brackets
n = 5
print('\n Generator expression:')
gen = (i for i in range(n))

# Using the generator expression
for num in gen:
    print(num)