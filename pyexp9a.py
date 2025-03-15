#ZAARA 231P023
stack=[]
def push():
    item = input("Enter item to push: ")
    stack.append(item)
    print(f"Item '{item}' pushed to stack")
def pop():
    if len(stack) == 0:
        print("Stack is empty! Cannot pop.")
    else:
        popped_item = stack.pop()
        print(f"Item '{popped_item}' popped from stack")
def display():
    if len(stack) == 0:
        print("Stack is empty!")
    else:
        print("Current stack:", stack)
def main():
    while True:
        print("\nMenu by Zaara :")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")        
        choice = input("Enter your choice: ")
        if choice == '1':
            push()
        elif choice == '2':
            pop()
        elif choice == '3':
            display()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
