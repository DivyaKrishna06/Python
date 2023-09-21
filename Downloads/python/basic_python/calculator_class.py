class Calculator:
    def add(self, x, y): # self variable points to an instance of the class when the method is revoked
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return ("Cannot divide by zero.")


calculator = Calculator()
n1=int(input('Enter 1st number: '))
n2=int(input('Enter 2nd number: '))

while True:
        print("\nSelect an option:")
        print("1. Addition")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. division")
        print("5. exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            result = calculator .add(n1,n2)
            print(f"{n1} + {n2} =", result)
        elif choice == "2":
            result = calculator.subtract(n1,n2)
            print(f"{n1} - {n2} =", result)
        elif choice == "3":
            result = calculator.multiply(n1,n2)
            print(f"{n1} x {n2} =", result)
        elif choice == "4":
            result = calculator.divide(n1,n2)
            print(f"{n1} / {n2} =", result)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")