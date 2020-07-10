# eBookstore
This is a project completed during a data science bootcamp hosted by Hyperiondev. 
The program was made to assist bookstore clerks by creating a database to store information of the books available instore. 
The program allows the clerk to add and remove books to the database, update book information and search for a specific book. 

## Prerequisites 
The program is written in python and uses SQLite to create a database. 
The program needs to be run in python 3 and sqlite3 must be imported. 

## Using the program 
The program was created to be used by a bookstore clerk and presents the user with the following menue: 

1. Enter book
2. Update book
3. Delete book
4. Search books
0. Exit 

The program peforms the function the user selects and stores the information in a table called 'books' in a database called 'ebookstore.' 

## The data 
The idea is that the user enters data that is relevant to them. Data is entered into the 'books' table by using the 'Enter book' or 'Update book' functions.
The for each book, the user must enter the title of the book, the author name, the quantity of books available in store and a unique identification number. 

## Author
Amy Marais

## Acknowledgements
The program was written as a task for a Hyperiondev data science bootcamp, and my mentor, Daniel Cornelius, helped me refine the program. 
