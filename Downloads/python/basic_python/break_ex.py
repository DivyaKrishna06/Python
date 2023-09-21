i=int(input('Enter the range:'))
print(f'Displays data from 1 to {i}')
print('1 is a prime number')
i+=1
for n in range(2, i):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        # loop fell through without finding a factor
        print(n, 'is a prime number')