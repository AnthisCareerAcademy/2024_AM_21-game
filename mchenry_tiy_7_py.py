import csv
filename = 'Chapter_7Challenge.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    name = []
    candy_type_1 = []
    candy_type_2 = []
    candy_price_1 = []
    candy_price_2 = []

    for row in reader:
        name = row[1]
        candy_1 = row[2]
        candy_2 = row[4]
        price_1 = float(row[3])
        price_2 = float(row[5])

