print(16.1)
#Save the following to books.csv file
'''
author,book
J R R Tolkien,The Hobbit
Lynne Truss,"Eats, Shoots & Leaves"
'''

print(16.2)
#Read the DictReader method to read in the file and save it to tge variable 'books'
import csv

with open("books.csv", "r") as csv1:
  text = csv1.read()

print(text)

#Question - Did DictReader handle the quotes and commas in the second book's title?
#It appears to be identical to the original CSV file.


#16.3
#Save the following to a books2.csv file
'''
title,author,year
The Weirdstone of Brisingamen, Alan Garner, 1960
Perdido Street Station, China Miéville, 2000
Thud!, Terry Pratchett, 2005
The Spellman Files,Lisa Lutz, 2007
Small Gods, Terry Pratchett, 1992
'''

#16.4
print(16.4)
#Use the sqlite3 module to create a SQLite database called book.db and a table called books with these fields: title(text), author (text), and year (integer)
import sqlite3

con = sqlite3.connect("books.db")
cur = con.cursor()
cur.execute('''CREATE TABLE books
(title VARCHAR(20),
author VARCHAR(20),
year INT)''')

#16.5
print(16.5)
#Read books2.csv and inset its data into the book table
with open("books2.csv", "rt") as csv2:
  bookData = csv.reader(csv2)
  books = [row for row in bookData]

del books[0]

insertSQLCommand = "Insert INTO books (title, author, year) VALUES(?, ?, ?)"
for book in books:
  cur.execute(insertSQLCommand, book)

#16.6
print(16.6)
#Select and print the title column from the book table in order of publication
cur.execute('SELECT title from books ORDER BY title')

for book in cur.fetchall():
    print(*book, sep=', ')

#16.7
print(16.7)
#Select and print the title column from the book table in order of year
cur.execute('SELECT * from books ORDER BY year')

for book in cur.fetchall():
    print(*book, sep=', ')

cur.close()
con.close()

#16.8
print(16.8)
#Select and print the title column from the book table in order of publication
import sqlalchemy as sqla

con = sqla.create_engine('sqlite:///books.db')
rows = con.execute('select title from books order by title asc')
for row in rows:
  print(rows)