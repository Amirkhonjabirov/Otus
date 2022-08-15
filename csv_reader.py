from csv import DictReader

books = []
with open('books.csv', newline='') as f:
    reader = DictReader(f)

    for row in reader:
        tmp = {
            'title': row['Title'],
            'author': row['Author'],
            'pages': row['Pages'],
            'genre': row['Genre']

        }
        books += [tmp]
