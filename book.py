class Book():

    favs = [];  #class variable to store favorite books

    #Book class constructor to initialize the book object with title, author, and pages
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    #methos to return a string representation of the book object
     #what happens when you pass object to print
    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

    def is_short(self):
        if self.pages < 100:
            return True
        else:
            return False

    #what happens when you use the == operator to compare two book objects
    def __eq__(self, other):
        if isinstance(other, Book):
            if self.title == other.title and self.author == other.author and self.pages == other.pages:
                return 
        return False

    #It's appropriate to give something for __hash__ when you override __eq__ because the hash value is used to determine the equality of objects in sets and dictionaries. If two objects are considered equal (i.e., they have the same hash value), they should also be considered equal when compared using the == operator. By providing a custom __hash__ method, you ensure that the hash value is consistent with the equality comparison defined in __eq__. This is important for maintaining the integrity of data structures that rely on hashing, such as sets and dictionaries.
    # Disable hashing for Book objects to prevent them from being used as dictionary keys or set elements  
    #This is the recommended way if mutable objects are used as keys in dictionaries or elements in sets. It prevents unexpected behavior when the object is modified after being added to a set or used as a key in a dictionary.
    __hash__ = None  

    def __repr__(self):
        return self.__str__();