import sqlite3

conn = sqlite3.connect("db.db")  # Create an in-memory database  

c = conn.cursor();

c.execute('''CREATE TABLE IF NOT EXISTS books
             (title TEXT, author TEXT, pages INTEGER)''');

c.execute("INSERT INTO books VALUES ('The Great Gatsby', 'F. Scott Fitzgerald', 180)");
c.execute("INSERT INTO books VALUES ('To Kill a Mockingbird', 'Harper Lee', 281)");
c.execute("INSERT INTO books VALUES ('1984', 'George Orwell', 328)");
c.execute("INSERT INTO books VALUES ('Pride and Prejudice', 'Jane Austen', 432)");  
c.execute("INSERT INTO books VALUES ('The Catcher in the Rye', 'J.D. Salinger', 277)");
c.execute("INSERT INTO books VALUES ('The Hobbit', 'J.R.R. Tolkien', 310)");
c.execute("INSERT INTO books VALUES ('The Lord of the Rings', 'J.R.R. Tolkien', 1178)");
c.execute("INSERT INTO books VALUES ('The Chronicles of Narnia', 'C.S. Lewis', 767)");

conn.commit();


c.execute("SELECT * FROM books");
rows = c.fetchall();
print("All books in the database:");
for row in rows:
    print(row); 


books = [("Are you my mother?", "P.D. Eastman", 24), 
         ("The Very Hungry Caterpillar", "Eric Carle", 32),
         ("Goodnight Moon", "Margaret Wise Brown", 32), 
         ("The Cat in the Hat", "Dr. Seuss", 61), 
         ("Green Eggs and Ham", "Dr. Seuss", 62), 
         ("Where the Wild Things Are", "Maurice Sendak", 48), 
         ("The Giving Tree", "Shel Silverstein", 64), 
         ("Corduroy", "Don Freeman", 32), 
         ("The Polar Express", "Chris Van Allsburg", 32), 
         ("The Snowy Day", "Ezra Jack Keats", 32)];

c.executemany("INSERT INTO books VALUES (?, ?, ?)", books);
conn.commit();

c.execute("SELECT * FROM books");
rows = c.fetchall();
print("All books in the database after inserting multiple records:");
#print(rows);

file = open("input.txt", 'w')
for row in rows:
    print(row);
    file.write(row[0] + "\t" + row[1] + "\t" + str(row[2]) + "\n");
file.close()


c.execute('DELETE FROM books WHERE title = "The Very Hungry Caterpillar"');
c.execute('DELETE FROM books WHERE title = "Are you my mother?"');
c.execute('DELETE FROM books WHERE title = "Where the Wild Things Are"');
conn.commit();

c.execute("SELECT * FROM books");
rows = c.fetchall();
print("All books in the database after deleting a record:");
print("===================================================");
for row in rows:    
    print(row[0] + "\t" + row[1] + "\t" + str(row[2]));