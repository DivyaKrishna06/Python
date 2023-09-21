n=int(input('Enter an integer for range:'))
n+=1
print('Integer\t ^2\t ^3')
for x in range(1, n):               #returns a printable representation of the object by converting that object to a string
    print(repr(x).rjust(5), repr(x*x).rjust(5), end=' ') # right justified - rjust (padding)
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(7))