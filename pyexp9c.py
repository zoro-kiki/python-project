#ZAARA 231P023

class LinkedList:
    def __init__(self):
        self.linked_list = [] 
    def insert(self, index, data):
        """Insert data at the specified index in the list."""
        try:
            self.linked_list.insert(index, data)
            print(f"Node with data '{data}' inserted at index {index}.")
        except IndexError:
            print("Invalid index! Insertion failed.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def delete(self, index):
        """Delete the node at the specified index."""
        try:
            deleted_item = self.linked_list.pop(index)
            print(f"Node with data '{deleted_item}' deleted.")
        except IndexError:
            print("Invalid index! Deletion failed.")
        except Exception as e:
            print(f"An error occurred: {e}")
    def display(self):
        """Display the entire linked list."""
        if not self.linked_list:
            print("The linked list is empty.")
        else:
            print("Linked List contents:")
            for index, item in enumerate(self.linked_list):
                print(f"Index {index}: {item}")
def menu():
    linked_list = LinkedList()
    while True:
        print("\nMenu by Zaara :")
        print("1. Insert")
        print("2. Delete")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            try:
                index = int(input("Enter index to insert: "))
                data = input("Enter data to insert: ")
                linked_list.insert(index, data)
            except ValueError:
                print("Invalid input! Please enter a valid index and data.")
        elif choice == '2':
            try:
                index = int(input("Enter index to delete: "))
                linked_list.delete(index)
            except ValueError:
                print("Invalid input! Please enter a valid index.")
        elif choice == '3':
            linked_list.display()
        
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    menu()

