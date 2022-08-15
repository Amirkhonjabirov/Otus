from csv import DictReader

books = []
with open('books.csv', newline='') as f:
    reader = DictReader(f)

    for row in reader:
        books += [row]
