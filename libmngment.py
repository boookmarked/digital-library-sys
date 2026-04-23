# Library Management System
# A Python project for managing a digital library using CSV
files
import csv
# File names
USERS_FILE = 'users.csv'
BOOKS_FILE = 'books.csv'
ISSUED_FILE = 'issued_books.csv'
NOTES_FILE = 'notes.csv'
REVIEWS_FILE = 'reviews.csv'
# Utility functions
def read_csv(file_name):
"""Reads data from a CSV file."""
try:
with open(file_name, mode='r') as file:
return [line.strip().split(',') for line in
file.readlines()]
except FileNotFoundError:
return []
def write_csv(file_name, rows):
"""Writes data to a CSV file."""
with open(file_name, mode='w') as file:
for row in rows:
file.write(','.join(row) + '\n')
# Admin Functions
def admin_login():
print("\n--- Admin Login ---")
username = input("Enter Admin Username: ")
password = input("Enter Admin Password: ")
if username == "apoorvi" and password == "6464":
print("Login Successful!\n")
return True
else:
print("Invalid Credentials.\n")
return False
def add_user():
print("\n--- Add User ---")
users = read_csv(USERS_FILE)
user_id = input("Enter User ID: ")
name = input("Enter User Name: ")
password = input("Enter Password: ")

9

users.append([user_id, name, password])
write_csv(USERS_FILE, users)
print("User added successfully!\n")
def delete_user():
print("\n--- Delete User ---")
users = read_csv(USERS_FILE)
user_id = input("Enter User ID to delete: ")
updated_users = [user for user in users if user[0] !=
user_id]
if len(updated_users) < len(users):
write_csv(USERS_FILE, updated_users)
print("User deleted successfully!\n")
else:
print("User ID not found.\n")
def view_users():
print("\n--- View All Users ---")
users = read_csv(USERS_FILE)
if users:
for user in users:
print(f"UserID: {user[0]}, Name: {user[1]}")
else:
print("No users found.\n")
def add_book():
print("\n--- Add Book ---")
books = read_csv(BOOKS_FILE)
book_id = input("Enter Book ID: ")
title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
genre = input("Enter Genre: ")
books.append([book_id, title, author, genre, ""])
write_csv(BOOKS_FILE, books)
print("Book added successfully!\n")
def delete_book():
print("\n--- Delete Book ---")
books = read_csv(BOOKS_FILE)
book_id = input("Enter Book ID to delete: ")
updated_books = [book for book in books if book[0] !=
book_id]
if len(updated_books) < len(books):
write_csv(BOOKS_FILE, updated_books)
print("Book deleted successfully!\n")
else:
print("Book ID not found.\n")
def view_books():
print("\n--- View All Books ---")
books = read_csv(BOOKS_FILE)

10

if books:
for book in books:
print(f"BookID: {book[0]}, Title: {book[1]},
Author: {book[2]}, Genre: {book[3]}, IssuedTo: {book[4]}")
else:
print("No books found.\n")
def issue_book():
print("\n--- Issue Book ---")
books = read_csv(BOOKS_FILE)
book_id = input("Enter Book ID to issue: ")
user_id = input("Enter User ID: ")
for book in books:
if book[0] == book_id:
if book[4]:
print(f"Book already issued to User ID:
{book[4]}.\n")
return
else:
book[4] = user_id

write_csv(BOOKS_FILE, books)

print("Book issued successfully!\n")
return
print("Book ID not found.\n")
def return_book():
print("\n--- Return Book ---")
books = read_csv(BOOKS_FILE)
book_id = input("Enter Book ID to return: ")
for book in books:
if book[0] == book_id:
if book[4]:
book[4] = ""
write_csv(BOOKS_FILE, books)

print("Book returned successfully!\n")

return
else:
print("Book is not issued to anyone.\n")
return
print("Book ID not found.\n")
# User Functions
def user_login():
print("\n--- User Login ---")
users = read_csv(USERS_FILE)
user_id = input("Enter User ID: ")
password = input("Enter Password: ")
for user in users:
if user[0] == user_id and user[2] == password:
print(f"Welcome, {user[1]}!\n")
return user_id

11

print("Invalid Credentials.\n")
return None
def search_books():
print("\n--- Search Books ---")
books = read_csv(BOOKS_FILE)
query = input("Enter book title, author, or genre to
search: ").lower()
results = [book for book in books if query in
book[1].lower() or query in book[2].lower() or query in
book[3].lower()]
if results:
print("\n--- Search Results ---")
for book in results:
print(f"BookID: {book[0]}, Title: {book[1]},
Author: {book[2]}, Genre: {book[3]}")
else:
print("No matching books found.\n")
def view_issued_books(user_id):
print("\n--- Issued Books ---")
books = read_csv(BOOKS_FILE)
issued_books = [book for book in books if book[4] ==
user_id]
if issued_books:
for book in issued_books:
print(f"BookID: {book[0]}, Title: {book[1]},
Author: {book[2]}")
else:
print("No books issued to you.\n")
# Additional Features
def add_notes():
print("\n--- Add Note ---")
notes = read_csv(NOTES_FILE)
note_id = input("Enter Note ID: ")
content = input("Enter Note Content: ")
notes.append([note_id, content])
write_csv(NOTES_FILE, notes)
print("Note added successfully!\n")
def view_notes():
print("\n--- View Notes ---")
notes = read_csv(NOTES_FILE)
if notes:
for note in notes:
print(f"NoteID: {note[0]}, Content: {note[1]}")
else:
print("No notes found.\n")
def add_review():

12

print("\n--- Add Book Review ---")
reviews = read_csv(REVIEWS_FILE)
book_id = input("Enter Book ID: ")
user_id = input("Enter User ID: ")
review_content = input("Enter Review Content: ")
reviews.append([book_id, user_id, review_content])
write_csv(REVIEWS_FILE, reviews)
print("Review added successfully!\n")
def view_reviews():
print("\n--- View All Reviews ---")
reviews = read_csv(REVIEWS_FILE)
if reviews:
for review in reviews:
print(f"BookID: {review[0]}, UserID: {review[1]},
Review: {review[2]}")
def search_notes():
print("\n--- Search Notes ---")
try:
with open(NOTES_FILE, "r") as file:
notes = file.readlines()
query = input("Enter keyword to search in notes:
").lower()
results = [note for note in notes if query in
note.lower()]
if results:
print("\n--- Search Results ---")
for note in results:
print(note.strip())
else:
print("No matching notes found.\n")
except FileNotFoundError:
print("No notes available.\n")
def delete_notes():
print("\n--- Delete Note ---")
try:
with open(NOTES_FILE, "r") as file:
notes = file.readlines()
note_id = input("Enter Note ID to delete: ")
updated_notes = [note for note in notes if not
note.startswith(note_id + ",")]
if len(updated_notes) < len(notes):
with open(NOTES_FILE, "w") as file:
file.writelines(updated_notes)
print("Note deleted successfully!\n")
else:
print("Note ID not found.\n")
except FileNotFoundError:
print("No notes to delete.\n")

13

# Main Program
def main():
while True:
print("\n--- Library Management System ---")
print("1. Admin Login")
print("2. User Login")
print("3. Exit")
choice = input("Enter your choice: ")
if choice == "1":
if admin_login():
while True:
print("\n--- Admin Panel ---")
print("1. Add User")
print("2. Delete User")
print("3. View Users")
print("4. Add Book")
print("5. Delete Book")
print("6. View Books")
print("7. Issue Book")
print("8. Return Book")
print("9. Logout")
admin_choice = input("Enter your choice:

")
if admin_choice == "1":
add_user()
elif admin_choice == "2":
delete_user()
elif admin_choice == "3":
view_users()
elif admin_choice == "4":
add_book()
elif admin_choice == "5":
delete_book()
elif admin_choice == "6":
view_books()
elif admin_choice == "7":
issue_book()
elif admin_choice == "8":
return_book()
elif admin_choice == "9":
break
else:
print("Invalid choice.\n")
elif choice == "2":
user_id = user_login()
if user_id:
while True:
print("\n--- User Panel ---")
print("1. Search Books")
print("2. View Issued Books")
print("3. Add Notes")

14

print("4. View Notes")
print("5. Search Notes")
print("6. Delete Notes")
print("7. Logout")
user_choice = input("Enter your choice: ")
if user_choice == "1":
search_books()
elif user_choice == "2":
view_issued_books(user_id)
elif user_choice == "3":
add_notes()
elif user_choice == "4":
view_notes()
elif user_choice == "5":
search_notes()
elif user_choice == "6":
delete_notes()
elif user_choice == "7":
break
else:
print("Invalid choice.\n")
elif choice == "3":
print("Exiting the system. Goodbye!")
break
else:
print("Invalid choice.\n")
# Run the program
if __name__ == "__main__":
main()
