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

def update_student(student_id, name):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Students SET name=%s WHERE student_id=%s", (name, student_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_student(student_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE student_id=%s", (student_id,))
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

def update_book(book_id, title, author):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Books SET title=%s, author=%s WHERE book_id=%s", (title, author, book_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_book(book_id):
    conn = connect_to_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Books WHERE book_id=%s", (book_id,))
    conn.commit()
    cursor.close()
    conn.close()


    
def add_student_input():
    name = input("Enter student's name: ")
    add_student(name)
    print(f"Student '{name}' added successfully.")

def update_student_input():
    student_id = input("Enter student ID: ")
    name = input("Enter new name for the student: ")
    update_student(student_id, name)
    print(f"Student ID '{student_id}' updated successfully.")

def delete_student_input():
    student_id = input("Enter student ID to delete: ")
    delete_student(student_id)
    print(f"Student ID '{student_id}' deleted successfully.")

def add_book_input():
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    add_book(title, author)
    print(f"Book '{title}' by '{author}' added successfully.")

def update_book_input ():
    book_id = input("Enter book ID to update: ")
    title = input("Enter new title: ")
    author = input("Enter new author: ")
    update_book(book_id, title, author)
    print(f"Book ID '{book_id}' updated successfully.")

def delete_book_input():
    book_id = input("Enter book ID to delete: ")
    delete_book(book_id)
    print(f"Book ID '{book_id}' deleted successfully.")

while True:
    print("\n--- Library Management System ---")
    print("1. Add Student")
    print("2. Update Student")
    print("3. Delete Student")
    print("4. Add Book")
    print("5. Update Book")
    print("6. Exit")

    choice = input("Enter your choice: ")
        
    if choice == '1':
        add_student_input()
    elif choice == '2':
        update_student_input()
    elif choice == '3':
        delete_student_input()
    elif choice == '4':
        add_book_input()
    elif choice == '5':
       update_book_input()
    elif choice == '6':
        delete_book_input()
    elif choice == '7':
        print("Exiting the system.")
        break
    else:
        print("Invalid choice, please try again.")