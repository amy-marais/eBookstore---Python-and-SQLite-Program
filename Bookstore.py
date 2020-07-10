#Capstone Project 1

#Create a data base called 'ebookstore'
import sqlite3
db = sqlite3.connect('data/ebookstore_db')
cursor = db.cursor()  

#Create a table called 'books'
cursor.execute('''
    CREATE TABLE books(id INTEGER PRIMARY KEY, Title TEXT, Author TEXT,
                   	Qty INTEGER)
''')
db.commit()

#Populate the table with the values given in the pdf
cursor = db.cursor()
id1 = 3001
Title1 = 'A Tale of Two Cities'
Author1 = 'Charles Dickens'
Qty1 = 30

id2 = 3002
Title2 = 'Harry Potter and the Philosopher\'s Stone'
Author2 = 'J.K. Rowling'
Qty2 = 40

id3 = 3003
Title3 = 'The Lion, the Witch and the Wardrobe'
Author3 = 'C.S. Lewis'
Qty3 = 25

id4 = 3004
Title4 = 'The Lord of the Rings'
Author4 = 'J.R.R. Tolkien'
Qty4 = 37

id5 = 3005
Title5 = 'Alice in Wonderland'
Author5 = 'Lewis Carroll'
Qty5 = 12

books_ = [(id1, Title1, Author1, Qty1), (id2, Title2, Author2, Qty2),
          (id3, Title3, Author3, Qty3), (id4, Title4, Author4, Qty4),
          (id5, Title5, Author5, Qty5)]
cursor.executemany(''' INSERT INTO books(id, Title, Author, Qty) VALUES(?,?,?,?)''', books_)
db.commit()

#Create different functions so that the user can enter, update, delete and search for books,
#as well as exit the program

#1. Enter Book
def EnterBook(id, Title, Author, Qty):
    cursor = db.cursor()
    id = input(int("Enter the book ID: "))
    Title = input("Enter the book title: ")
    Author = input("Enter the author's name: ")
    Qty = input(int("Enter the quantity of " + Title + " books that are in stock: "))
    cursor.execute(''' INSERT INTO books (id, Title, Author, Qty) VALUES (?,?,?,?)''', (id, Title, Author, Qty))
    db.commit()
    return print( Title + " written by " + Author + " has been added to the ebookstore with ID number " + str(id) + " with " + str(Qty) + " books in stock.")

#2. Update Book
def UpdateBook (id, Title, Author, Qty):
    cursor = db.cursor()
    Title = input(int("Please enter the title of the book you would like to update: "))
    variable = input("What would you like to update about \"" + Title1 + "\" - ID/Title/Author/Quantity :")

    #Updating the book's ID number
    if variable == "ID":
        id = input(str("Please enter the new ID number for \"" + Title + "\" : "))
        cursor.execute(''' UPDATE books SET id = ? WHERE Title = ?''', (id, Title))
        db.commit()
        return print(Title + " has successfully been updated, and now has the ID number " + str(id) + ".")

    #Updating the book's title
    elif variable == "Title":
        Title2 = input(str("Please enter the updated title for \"" + Title + "\" : "))
        cursor.execute(''' UPDATE books SET Title = ? WHERE Title = ?''', (Title2, Title))
        db.commit()
        return print("\"" + Title + "\" has successfully been updated to be \"" + Title2 + ".\"")

    #Updating the book's author
    elif variable == "Author":
        Author = input(str("Please enter the new author name for \"" + Title + "\" :"))
        cursor.execute(''' UPDATE books SET Author = ? WHERE Title = ?''', (Author, Title))
        db.commit()
        return print("\"" + Title + "\" has successfully been updated, and now has the author \"" + Author + ".\"")

    #Updating the quantity of stock
    elif variable == "Quantity":
        Qty = input(int("Please enter the quantity of \"" + Title + "\" that is currently in stock: "))
        cursor.execute(''' UPDATE books SET Quantity = ? WHERE Title = ?''', (Qty, Title))
        db.commit()
        return print("\"" + Title + "\" has successfully been updated, and has a stock of " + str(Qty) + " books.")

    #error message
    else:
        return print("This is not a recognised request. Please start again.")
    

#3. Delete Book
def DeleteBook (id):
    cursor = db.cursor()
    id = input(int("Please enter the ID number of the book you want to delete: "))
    cursor.execute('''DELETE FROM books WHERE id = ?''', (id,))
    db.commit()
    return print ("The book with the ID number " + str(id) + " has successfully been deleted from the ebookstore.")

#4. Search Books
def SearchBook (id, Title, Author):
    cursor = db.cursor()
    searchkey = input(str("Please enter the key you would like to use to search for a book - ID/Title/Author?"))

    #Searching for a book via its ID number
    if searchkey == "ID":
        id = input(int("Please enter the ID number of the book you are looking for : "))
        cursor.execute('''SELECT id, Title, Author, Qty from books WHERE id = ?''', (id,))
        bookinfo = cursor.fetchone()
        return print(bookinfo)
        
    #Searching for a book via its title
    elif searchkey == "Title":
        Title = input("Please enter the title of the book you are looking for : ")
        cursor.execute('''SELECT id, Title, Author, Qty from books WHERE Title = ?''', (Title,))
        bookinfo = cursor.fetchone()
        return print(bookinfo)
        
    #Searching for a book via the author's name
    elif searchkey == "Author":
        Author = input("Please enter the name of the author of the book you're looking for:")
        cursor.execute('''SELECT id, Title, Author, Qty from books WHERE Author = ?''', (Author,))
        bookinfo = cursor.fetchall()
        print("Here is a list of books written by " + str(Author) + " : ")
        return print(bookinfo)
        
    #error message
    else:
        return print("This is not a recognised searchkey. Please start again.")

   
#0. Exit
def ExiteBookstore():
    db.close()
    return print("You have left the ebookstore.")


#Making a menue and calling on the functions

print("Hello and welcome to the ebookstore! Here is a list of actions you can perform in the bookstore :")
print(" ")
print("1. Enter a book")
print("2. Update a book")
print("3. Delete a book")
print("4. Search for a book")
print("0. Exit the ebookstore")
print(" ")
action = input(str("Please enter the number that corresponds with the action you want to perform : "))

#Call on the EnterBook function
if action == "1" or "1.":
    EnterBook()
    action = input(str("Please enter the number that corresponds with the action you want to perform : "))

#Call on the UpdateBook function
elif action == "2" or "2.":
    UpdateBook()
    action = input(str("Please enter the number that corresponds with the action you want to perform : "))

#Call on the DeleteBook function
elif action == "3" or "3.":
    DeleteBook()
    action = input(str("Please enter the number that corresponds with the action you want to perform : "))

#Call on the SearchBook function
elif action == "4" or "4.":
    SearchBook()
    action = input(str("Please enter the number that corresponds with the action you want to perform : "))

#Call on the ExiteBookstore function
elif action == "0" or "0.":
    ExiteBookstore()

#Error message
else:
    print("This action is not recognised.")
    action = input(str("Please enter the number that corresponds with the action you want to perform : "))
