from book import Book
import booksSDK

book = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
print(booksSDK.add_book(book))


print(booksSDK.get_books())
#print(booksSDK.get_books())