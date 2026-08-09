import sqlite3
from book import Book


def cursor():
    return sqlite3.connect("books.db").cursor()  # Create an in-memory database

c = cursor();

c.execute('''CREATE TABLE IF NOT EXISTS books
             (title TEXT, author TEXT, pages INTEGER)''');
c.connection.close();


def add_book(book):
    c = cursor();
    c.execute("INSERT INTO books VALUES (?, ?, ?)", (book.title, book.author, book.pages));
    c.connection.commit();
    c.connection.close();
    return f"Book '{book.title}' added successfully on row {c.lastrowid}."

def get_books():
    c = cursor();
    c.execute("SELECT * FROM books");
    rows = c.fetchall();
    c.connection.close();
    return rows