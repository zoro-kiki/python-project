#Zaara 231P023
queue = []
def insert():
    item = input("Enter item to insert: ")
    queue.append(item)
    print(f"Item '{item}' inserted into queue")
def delete():
    if len(queue) == 0:
        print("Queue is empty! Cannot delete.")
    else:
        deleted_item = queue.pop(0)
        print(f"Item '{deleted_item}' deleted from queue")
def display():
    if len(queue) == 0:
        print("Queue is empty!")
    else:
        print("Current queue:", queue)
def main():
    while True:
        print("\nMenu by Zaara:")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            insert()
        elif choice == '2':
            delete()
        elif choice == '3':
            display()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
