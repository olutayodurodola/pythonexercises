class book():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}, {self.pages} pages"

Book = book("The Great Gatsby", "F. Scott Fitzgerald", 180);

print(Book.title);
print(Book.__str__());
print(type(Book));
print(Book);


file = open("input.txt", 'w')
file.write("Visual c++\tAndrew Young\t65\nIt contains some sample text.\t1009\nThis is the third line of the file.\t560")
file.close()


file = open("input.txt", 'r')
content = file.read().split("\n")
file.close()

print(content)

book_data = content[0].split("\t");
print(book_data);
book1 = book(book_data[0], book_data[1], int(book_data[2]));
book2 = book(content[1].split("\t")[0], "Unknown Author", int(content[1].split("\t")[1]));
book3 = book(content[2].split("\t")[0], "Unknown Author", int(content[2].split("\t")[1]));
print(book1);
print(book2);
print(book3);

"""
try:
    with open("input.txt", 'r') as file:
        int(content = file.read().split("\n"));
        print(content);
except Exception as e:
    print(f"An error occurred: {e}");

"""

#Another example of using the try-except block to handle exceptions when reading a file
try:
    file = open("input.txt");
    print("File opened successfully.");
except OSError as e:
    print(f"An error occurred: {e}");
else:
    with file:
        try:
            file.read();
        except Exception as e:
            print(f"An error occurred while reading the file: {e}");
