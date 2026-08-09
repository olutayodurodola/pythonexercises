class Books(object):
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_book_info(self):
        return f"{self.title} by {self.author}, published in {self.year}"

###### Passing objects by reference to a function ######

book = Books("To Kill a Mockingbird", "Harper Lee", 1960);
print(book.get_book_info());

def modify(book):
    book.title = "1984"
    book.author = "George Orwell"
    book.year = 1949
    print(id(book));

modify(book);
print(book.get_book_info());

#What is the print id to follow?

def modify(book):
    print(id(book));
    book.title = "Changed noob";
    print(id(book));
    print(book, book.title,book.get_book_info());

modify(book);
print(id(book));