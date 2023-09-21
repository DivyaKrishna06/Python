i=int(input('Enter the range:'))
print(f'Displays data from 1 to {i}')
i+=1
for num in range(1, i):
    if num % 2 == 0:
        print(f"{num} is an even number")
        continue
    print(f"{num} is an odd number")