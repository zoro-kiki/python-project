#ZAARA231P023
import mysql.connector
def connect():
    return mysql.connector.connect(host="localhost", user="root", password="root", database="society")
def setup():
    conn = mysql.connector.connect(host="localhost", user="root", password="root")
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS society")
    conn.close()
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            flat_no VARCHAR(10),
            dues DECIMAL(10,2)
        )
    """)
    conn.close()
def insert_member():
    name = input("Enter name: ")
    flat_no = input("Enter flat number: ")
    dues = float(input("Enter dues: "))

    conn = connect()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (name, flat_no, dues) VALUES (%s, %s, %s)", (name, flat_no, dues))
    conn.commit()
    conn.close()
    print("Member added.")
def display_members():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    for row in cursor.fetchall():
        print(row)
    conn.close()

# Menu by Zaara231P023
def menu():
    setup()
    while True:
        choice = input("\n1. Add Member\n2. View Members\n3. Exit\nChoose: ")
        if choice == '1':
            insert_member()
        elif choice == '2':
            display_members()
        elif choice == '3':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
