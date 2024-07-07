import csv
import os

def loadBooks():
    bookList = {}
    file_path = os.path.join(os.path.dirname(__file__), 'bookList.csv')
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['id'] not in bookList:
                bookList[row['id']] = [[row['books'], row['location'], row['date']]]
            else:
                bookList[row['id']].append([row['books'], row['location'], row['date']])
    return bookList

def addBook(id, book, location, date):
    file_path = os.path.join(os.path.dirname(__file__), 'bookList.csv')
    with open(file_path, 'a', newline='') as csvfile:
        fieldnames = ['id', 'book', 'location', 'date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if csvfile.tell() == 0:
            writer.writeheader()
        writer.writerow({'id': id, 'book': book, 'location': location, 'date': date})

def main():
    id = 'test&1234567'
    book = 'Book 1'
    location = 'Location 2'
    date = '2024-07-07 20:59:56'
    print(loadBooks())
    addBook(id, book, location, date)

if __name__ == '__main__':
    main()