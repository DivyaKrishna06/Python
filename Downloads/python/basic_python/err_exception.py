def divide_numbers():
    try:
        # Ask the user for two numbers
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))

        # Attempt to perform the division
        result = numerator / denominator

        # Print the result
        print(f"Result of division: {numerator} / {denominator} = {result}")

    except ValueError:
        print("Error: Invalid input. Please enter valid numeric values.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    finally:
        print("Execution completed.")

if __name__ == "__main__":
    divide_numbers()