import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="lms"
)

def add_student(name):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name) VALUES (%s)", (name,))
    conn.commit()
    cursor.close()
    conn.close()

def add_book(title, author):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Books (title, author) VALUES (%s, %s)", (title, author))
    conn.commit()
    cursor.close()
    conn.close()
    
def add_student_input():
    name = input("Enter student's name: ")
    add_student(name)
    print(f"Student '{name}' added successfully.")

def add_book_input():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    add_book(title, author)
    print(f"Book '{title}' by '{author}' added successfully.")

while True:
    print("\n--- Library Management System ---")
    print("1. Add Student")
    print("2. Add Book")
    print("3. Exit")

    choice = input("Enter your choice: ")
        
    if choice == '1':
        add_student_input()
    elif choice == '2':
        add_book_input()
    elif choice == '0':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice, please try again.")