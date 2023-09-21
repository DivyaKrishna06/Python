class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def size(self):
        return len(self.items)

def main():
    stack = Stack()

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Quit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            item = input("Enter the item to push onto the stack: ")
            stack.push(item)
            print(f"{item} pushed onto the stack.")
        elif choice == '2':
            popped_item = stack.pop()
            print(f"Popped item: {popped_item}")
        elif choice == '3':
            peeked_item = stack.peek()
            print(f"Top item: {peeked_item}")
        elif choice == '4':
            stack_size = stack.size()
            print(f"Stack size: {stack_size}")
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
